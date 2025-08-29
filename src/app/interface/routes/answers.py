from logging import getLogger

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException

from app.application.commands import CreateAnswerIteractor, RemoveAnswerIteractor
from app.application.queries import GetAnswerIteractor
from app.interface.schemas.answers import AnswerRequest, AnswerResponse

logger = getLogger(__name__)
router = APIRouter(tags=["Answers"], route_class=DishkaRoute)


@router.post("/questions/{id}/answers")
def create_answer(
    id: int,
    body: AnswerRequest,
    interactor: FromDishka[CreateAnswerIteractor]
) -> AnswerResponse:
    """Добавить ответ к вопросу"""
    answer = interactor.execute(id, body)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")
    return answer


@router.get("/answers/{id}")
def get_answer(id: int, interactor: FromDishka[GetAnswerIteractor]) -> AnswerResponse:
    """Получить конкретный ответ"""
    answer = interactor.execute(id)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Answer with id {id} not found")
    return answer


@router.delete("/answers/{id}")
def remove_answer(id: int, interactor: FromDishka[RemoveAnswerIteractor]) -> AnswerResponse:
    """Удалить ответ"""
    answer = interactor.execute(id)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Answer with id {id} not found")
    return answer
