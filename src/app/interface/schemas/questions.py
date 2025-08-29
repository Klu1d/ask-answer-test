from datetime import datetime

from pydantic import BaseModel, constr

from app.interface.schemas.answers import AnswerResponse


class QuestionRequest(BaseModel):
    text: str = constr(min_length=1, strip_whitespace=True)


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime


class QuestionWithAnswersResponse(BaseModel):
    question: QuestionResponse
    answers: list[AnswerResponse]
