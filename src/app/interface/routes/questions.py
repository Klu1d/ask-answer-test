from logging import getLogger

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException

from app.application.commands import CreateQuestionIteractor, RemoveQuestionIteractor
from app.application.queries import GetAllQuestionsIteractor, GetQuestionIteractor
from app.interface.schemas.questions import (
    QuestionRequest,
    QuestionResponse,
    QuestionWithAnswersResponse,
)

logger = getLogger(__name__)
router = APIRouter(tags=["Questions"], prefix="/questions", route_class=DishkaRoute)


@router.get("/")
def get_all_questions(interactor: FromDishka[GetAllQuestionsIteractor]):
    """Cписок всех вопросов"""
    questions = interactor.execute()
    return questions


@router.post("/")
def create_question(
    body: QuestionRequest, interactor: FromDishka[CreateQuestionIteractor]
) -> QuestionResponse:
    """Cоздать новый вопрос"""
    question = interactor.execute(body)
    return question


@router.get("/{id}")
def get_question(
    id: int, interactor: FromDishka[GetQuestionIteractor]
) -> QuestionWithAnswersResponse:
    """Получить вопрос и все ответы на него"""
    question = interactor.execute(id)
    if question is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")
    return question


@router.delete("/{id}")
def remove_question(id: int, interactor: FromDishka[RemoveQuestionIteractor]) -> QuestionRequest:
    """Удалить вопрос"""
    question = interactor.execute(id)
    if question is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")
    return question
