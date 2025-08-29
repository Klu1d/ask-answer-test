from app.application.common.dto import (
    AnswerResponse,
    QuestionResponse,
    QuestionWithAnswersResponse,
)
from app.application.common.gateway import Gateway


class GetQuestionIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> QuestionWithAnswersResponse:
        result = self._gateway.get_question(id)
        if not result:
            return result

        question, answers = result
        return QuestionWithAnswersResponse(
            question=QuestionResponse(
                id=question.id, text=question.text, created_at=question.created_at
            ),
            answers=[
                AnswerResponse(
                    id=a.id,
                    text=a.text,
                    user_id=a.user_id,
                    question_id=a.question_id,
                    created_at=a.created_at,
                )
                for a in answers
            ],
        )
