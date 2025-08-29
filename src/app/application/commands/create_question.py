import logging

from app.application.common.dto import QuestionRequest, QuestionResponse
from app.application.common.gateway import Gateway
from app.domain.entities import Question

logger = logging.getLogger(__name__)

class CreateQuestionIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, body: QuestionRequest) -> QuestionResponse:
        logger.info("Request to add a new question")
        question: Question = self._gateway.create_question(body.text)
        return QuestionResponse(
            id=question.id,
            text=question.text,
            created_at=question.created_at,
        )
