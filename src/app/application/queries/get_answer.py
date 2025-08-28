from app.application.common.gateway import Gateway
from app.application.common.dto import AnswerResponse


class GetAnswerIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> AnswerResponse:
        answer = self._gateway.get_answer(id)
        return AnswerResponse(
            id=answer.id,
            text=answer.text,
            user_id=answer.user_id,
            created_at=answer.created_at,
            question_id=answer.question_id,
        )
