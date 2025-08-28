from app.application.commands import CreateQuestionIteractor, RemoveQuestionIteractor
from app.application.queries import GetQuestionIteractor, GetAllQuestionsIteractor
from fastapi import APIRouter

router = APIRouter(tags=["Questions"], prefix="questions")


@router.get("/")
def get_all_questions(id: int):
    """Cписок всех вопросов"""
    pass


@router.post("/")
def create_question(id: int):
    """Cоздать новый вопрос"""
    pass


@router.get("/{id}")
def get_question(id: int):
    """Получить вопрос и все ответы на него"""
    pass


@router.delete("/{id}")
def remove_question(id: int):
    """Удалить вопрос"""
    pass
