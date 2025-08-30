from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AnswerRequest(BaseModel):
    user_id: UUID
    text: str


class AnswerResponse(BaseModel):
    id: int
    text: str
    user_id: UUID
    question_id: int
    created_at: datetime
