from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(eq=False, kw_only=True)
class Question:
    id: int
    text: str
    created_at: datetime


@dataclass(eq=False, kw_only=True)
class Answer:
    id: int
    text: str
    user_id: UUID
    question_id: int
    created_at: datetime
