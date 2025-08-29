from uuid import UUID

from sqlalchemy.orm import Session

from app.application.common.gateway import Gateway
from app.domain.entities import Answer, Question
from app.infrastructure.models.answers import Answers
from app.infrastructure.models.questions import Questions


class SQLAlchemyGateway(Gateway):
    def __init__(self, session: Session):
        self.session = session

    def get_all_questions(self) -> list[Question]:
        rows = self.session.query(Questions).all()
        return [self._to_domain_question(row) for row in rows]

    def get_question(self, id: int) -> tuple[Question, list[Answer]] | None:
        row = self.session.query(Questions).filter_by(id=id).one_or_none()
        if row is None:
            return row
        question = self._to_domain_question(row)
        answers = [self._to_domain_answer(a) for a in row.answers]
        return question, answers

    def get_answer(self, id: int) -> Answer | None:
        row = self.session.query(Answers).filter_by(id=id).one_or_none()
        if row is None:
            return row
        return self._to_domain_answer(row)

    def create_question(self, text: str) -> Question:
        row = Questions(text=text)
        self.session.add(row)
        self.session.commit()
        return self._to_domain_question(row)

    def create_answer(self, question_id: int, user_id: UUID, text: str) -> Answer | None:
        if self.get_question(question_id) is None:
            return None
        row = Answers(question_id=question_id, user_id=str(user_id), text=text)
        self.session.add(row)
        self.session.commit()
        return self._to_domain_answer(row)

    def remove_answer(self, id: int) -> Answer | None:
        row = self.session.query(Answers).filter_by(id=id).one_or_none()
        if row is None:
            return row
        self.session.delete(row)
        self.session.commit()
        return self._to_domain_answer(row)

    def remove_question(self, id: int) -> Question | None:
        row = self.session.query(Questions).filter_by(id=id).one_or_none()
        if row is None:
            return row
        self.session.delete(row)
        self.session.commit()
        return self._to_domain_question(row)

    def _to_domain_question(self, row: Questions) -> Question:
        return Question(
            id=row.id,
            text=row.text,
            created_at=row.created_at,
        )

    def _to_domain_answer(self, row: Answers) -> Answer:
        return Answer(
            id=row.id,
            question_id=row.question_id,
            user_id=UUID(row.user_id),
            text=row.text,
            created_at=row.created_at,
        )
