from datetime import datetime

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
