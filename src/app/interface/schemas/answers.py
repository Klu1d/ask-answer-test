from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, constr


class AnswerRequest(BaseModel):
    # question_id: int
    user_id: UUID
    text: str = constr(min_length=1, strip_whitespace=True)


class AnswerResponse(BaseModel):
    id: int
    text: str
    user_id: UUID
    question_id: int
    created_at: datetime
