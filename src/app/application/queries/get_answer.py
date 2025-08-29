import logging

from app.application.common.dto import AnswerResponse
from app.application.common.gateway import Gateway

logger = logging.getLogger(__name__)


class GetAnswerIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> AnswerResponse | None:
        logger.info("Request to get answer with id=%s", id)
        answer = self._gateway.get_answer(id)
        
        if not answer:
            logger.warning("Answer with id=%s not found", id)
            return None

        logger.info("Answer with id=%s retrieved successfully", id)

        return AnswerResponse(
            id=answer.id,
            text=answer.text,
            user_id=answer.user_id,
            created_at=answer.created_at,
            question_id=answer.question_id,
        )
