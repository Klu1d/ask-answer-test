from datetime import datetime

from pydantic import BaseModel

from app.interface.schemas.answers import AnswerResponse


class QuestionRequest(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime


class QuestionWithAnswersResponse(BaseModel):
    question: QuestionResponse
    answers: list[AnswerResponse]
