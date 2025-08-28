from abc import ABC, abstractmethod

from app.domain.entities import Answer, Question
from uuid import UUID


class Gateway(ABC):
    @abstractmethod
    def get_all_questions(self) -> list[Question]:
        pass

    @abstractmethod
    def get_question(self, id: int) -> tuple[Question, list[Answer]]:
        pass

    @abstractmethod
    def get_answer(self, id: int) -> Answer:
        pass

    @abstractmethod
    def create_question(self, text: str) -> Question:
        pass

    @abstractmethod
    def create_answer(self, question_id: int, user_id: UUID, text: str) -> Answer:
        pass

    @abstractmethod
    def remove_question(self, id: int) -> None:
        pass

    @abstractmethod
    def remove_answer(self, id: int) -> None:
        pass
