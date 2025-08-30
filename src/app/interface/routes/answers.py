from logging import getLogger

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException

from app.application.commands import CreateAnswerInteractor, RemoveAnswerInteractor
from app.application.queries import GetAnswerInteractor
from app.interface.schemas.answers import AnswerRequest, AnswerResponse

logger = getLogger(__name__)
router = APIRouter(tags=["Answers"], route_class=DishkaRoute)


@router.post("/questions/{id}/answers")
def create_answer(
    id: int,
    body: AnswerRequest,
    interactor: FromDishka[CreateAnswerInteractor]
) -> AnswerResponse:
    """Добавить ответ к вопросу"""

    text = body.text.strip()
    if not text:
        raise HTTPException(status_code=422, detail="Answer cannot be empty or contain only whitespace")

    if len(text) < 4:
        raise HTTPException(status_code=422, detail="Answer must be at least 4 characters long")

    answer = interactor.execute(id, body)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Question with id {id} not found")

    return answer


@router.get("/answers/{id}")
def get_answer(id: int, interactor: FromDishka[GetAnswerInteractor]) -> AnswerResponse:
    """Получить конкретный ответ"""
    answer = interactor.execute(id)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Answer with id {id} not found")
    return answer


@router.delete("/answers/{id}")
def remove_answer(id: int, interactor: FromDishka[RemoveAnswerInteractor]) -> AnswerResponse:
    """Удалить ответ"""
    answer = interactor.execute(id)
    if answer is None:
        raise HTTPException(status_code=404, detail=f"Answer with id {id} not found")
    return answer
