from app.application.commands import CreateAnswerIteractor, RemoveAnswerIteractor
from app.application.queries import GetAnswerIteractor
from fastapi import APIRouter

router = APIRouter(tags=["Answers"])


@router.post("/questions/{id}/answers")
def create_answer(id: int):
    """Добавить ответ к вопросу"""
    pass


@router.get("/answers/{id}")
def get_answer(id: int):
    """Получить конкретный ответ"""
    pass


@router.remove("/answers/{id}")
def remove_answer(id: int):
    """Удалить ответ"""
    pass
