from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class QuestionRequest:
    text: str


@dataclass(slots=True)
class AnswerRequest:
    # question_id: int
    user_id: UUID
    text: str


@dataclass(slots=True)
class QuestionResponse:
    id: int
    text: str
    created_at: datetime


@dataclass(slots=True)
class AnswerResponse:
    id: int
    text: str
    user_id: UUID
    question_id: int
    created_at: datetime


@dataclass(slots=True)
class QuestionWithAnswersResponse:
    question: QuestionResponse
    answers: list[AnswerResponse]
