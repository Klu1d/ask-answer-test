from logging import getLogger

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException

from app.application.commands import CreateQuestionInteractor, RemoveQuestionInteractor
from app.application.queries import GetAllQuestionsInteractor, GetQuestionInteractor
from app.interface.schemas.questions import (
    QuestionRequest,
    QuestionResponse,
    QuestionWithAnswersResponse,
)

logger = getLogger(__name__)
router = APIRouter(tags=["Questions"], prefix="/questions", route_class=DishkaRoute)


@router.get("/")
def get_all_questions(interactor: FromDishka[GetAllQuestionsInteractor]):
    """Cписок всех вопросов"""
    questions = interactor.execute()
    return questions


@router.post("/")
def create_question(
    body: QuestionRequest, interactor: FromDishka[CreateQuestionInteractor]
) -> QuestionResponse:
    """Cоздать новый вопрос"""
    question = interactor.execute(body)
    return question


@router.get("/{id}")
def get_question(
    id: int, interactor: FromDishka[GetQuestionInteractor]
) -> QuestionWithAnswersResponse:
    """Получить вопрос и все ответы на него"""
    question = interactor.execute(id)
    if question is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")
    return question


@router.delete("/{id}")
def remove_question(id: int, interactor: FromDishka[RemoveQuestionInteractor]) -> QuestionRequest:
    """Удалить вопрос"""
    question = interactor.execute(id)
    if question is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")
    return question
