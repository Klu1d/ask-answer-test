from dataclasses import dataclass


@dataclass(eq=False)
class NotFoundError(Exception):
    @property
    def message(self) -> str:
        return "Entity not found"


@dataclass(eq=False)
class QuestionNotFoundError(NotFoundError):
    pass


@dataclass(eq=False)
class AnswerNotFoundError(NotFoundError):
    pass
