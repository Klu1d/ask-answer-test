import os
from datetime import datetime, timezone
from unittest.mock import patch
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_PORT"] = "5432"
os.environ["POSTGRES_USER"] = "test"
os.environ["POSTGRES_PASSWORD"] = "test"
os.environ["POSTGRES_DB"] = "test"


@pytest.fixture(scope="session")
def client():
    from app.__main__ import get_fastapi_app

    app = get_fastapi_app()
    return TestClient(app)


def test_create_answer_success(client):
    with patch("app.application.commands.CreateAnswerInteractor.execute") as mock:
        mock.return_value = {
            "id": 1,
            "question_id": 1,
            "user_id": str(uuid4()),
            "text": "тестовый ответ",
            "created_at": datetime.now(timezone.utc),
        }

        body = {"user_id": str(uuid4()), "text": "тестовый ответ"}
        resp = client.post("/questions/1/answers", json=body)

        assert resp.status_code == 200
        data = resp.json()
        assert data["text"] == "тестовый ответ"
        assert "id" in data
        assert "question_id" in data
        assert "created_at" in data


def test_create_answer_not_found(client):
    with patch("app.application.commands.CreateAnswerInteractor.execute") as mock:
        mock.return_value = None

        body = {"user_id": str(uuid4()), "text": "тестовый ответ"}
        resp = client.post("/questions/9999/answers", json=body)

        assert resp.status_code == 404
        data = resp.json()
        assert data["detail"] == "Question with id 9999 not found"


def test_get_all_questions_success(client):
    with patch("app.application.queries.GetAllQuestionsInteractor.execute") as mock:
        mock.return_value = [
            {
                "id": 1,
                "user_id": str(uuid4()),
                "title": "Первый вопрос",
                "text": "Текст первого вопроса",
                "created_at": datetime.now(timezone.utc),
            },
            {
                "id": 2,
                "user_id": str(uuid4()),
                "title": "Второй вопрос",
                "text": "Текст второго вопроса",
                "created_at": datetime.now(timezone.utc),
            },
        ]

        resp = client.get("/questions/")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 2
        assert data[0]["title"] == "Первый вопрос"
        assert data[1]["title"] == "Второй вопрос"


def test_get_all_questions_empty_list(client):
    with patch("app.application.queries.GetAllQuestionsInteractor.execute") as mock:
        mock.return_value = []

        resp = client.get("/questions/")
        assert resp.status_code == 200
        data = resp.json()
        assert len(data) == 0


def test_create_question_success(client):
    with patch("app.application.commands.CreateQuestionInteractor.execute") as mock:
        mock.return_value = {
            "id": 1,
            "user_id": str(uuid4()),
            "text": "Текст нового вопроса",
            "created_at": datetime.now(timezone.utc),
        }

        body = {"user_id": str(uuid4()), "text": "Текст нового вопроса"}
        resp = client.post("/questions/", json=body)
        assert resp.status_code == 200
        data = resp.json()
        assert data["text"] == "Текст нового вопроса"
        assert "id" in data
        assert "created_at" in data


def test_get_question_success(client):
    with patch("app.application.queries.GetQuestionInteractor.execute") as mock:
        mock.return_value = {
            "question": {
                "id": 1,
                "text": "Текст вопроса",
                "created_at": datetime.now(timezone.utc),
            },
            "answers": [
                {
                    "id": 1,
                    "user_id": str(uuid4()),
                    "text": "Первый ответ",
                    "question_id": 1,
                    "created_at": datetime.now(timezone.utc),
                }
            ],
        }

        resp = client.get("/questions/1")
        assert resp.status_code == 200

        data = resp.json()
        assert data["question"]["id"] == 1
        assert "answers" in data
        assert len(data["answers"]) == 1


def test_get_question_not_found(client):
    with patch("app.application.queries.GetQuestionInteractor.execute") as mock:
        mock.return_value = None

        resp = client.get("/questions/9999")
        assert resp.status_code == 404
        data = resp.json()
        assert data["detail"] == "Question with id 9999 not found"


def test_remove_question_success(client):
    with patch("app.application.commands.RemoveQuestionInteractor.execute") as mock:
        mock.return_value = {"text": "Текст удаленного вопроса"}

        resp = client.delete("/questions/1")
        assert resp.status_code == 200
        data = resp.json()
        assert data["text"] == "Текст удаленного вопроса"


def test_remove_question_not_found(client):
    with patch("app.application.commands.RemoveQuestionInteractor.execute") as mock:
        mock.return_value = None

        resp = client.delete("/questions/9999")
        assert resp.status_code == 404
        data = resp.json()
        assert data["detail"] == "Question with id 9999 not found"
