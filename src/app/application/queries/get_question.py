from app.application.common.gateway import Gateway
from app.application.common.dto import QuestionResponse


class GetQuestionIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> QuestionResponse:
        question = self._gateway.get_question(id)
        return QuestionResponse(
            id=question.id,
            text=question.text,
            user_id=question.user_id,
            created_at=question.created_at,
        )
