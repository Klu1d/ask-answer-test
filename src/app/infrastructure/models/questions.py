from datetime import datetime
from sqlalchemy import func, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.models.base import Base


class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    answers = relationship(
        "Answers", back_populates="question", cascade="all, delete-orphan"
    )
