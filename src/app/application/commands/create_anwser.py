from app.application.common.dto import AnswerRequest, AnswerResponse
from app.application.common.gateway import Gateway
from app.domain.entities import Answer


class CreateAnswerIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int, body: AnswerRequest) -> AnswerResponse:
        answer: Answer = self._gateway.create_answer(
            question_id=id,
            user_id=body.user_id,
            text=body.text,
        )
        if answer is None:
            return answer
        return AnswerResponse(
            id=answer.id,
            text=answer.text,
            user_id=answer.user_id,
            created_at=answer.created_at,
            question_id=answer.question_id,
        )
