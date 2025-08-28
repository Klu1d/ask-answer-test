from datetime import datetime
from sqlalchemy import func, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.models.base import Base


class Answers(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"))
    user_id: Mapped[str] = mapped_column(String(36)) # 36 символов под UUID
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    question = relationship("Questions", back_populates="answers")
