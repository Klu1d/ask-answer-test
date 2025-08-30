import logging

from app.application.common.dto import (
    AnswerResponse,
    QuestionResponse,
    QuestionWithAnswersResponse,
)
from app.application.common.gateway import Gateway

logger = logging.getLogger(__name__)


class GetQuestionInteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> QuestionWithAnswersResponse | None:
        logger.info("Request to get question with id=%s", id)
        result = self._gateway.get_question(id)

        if not result:
            logger.warning("Question with id=%s not found", id)
            return None

        question, answers = result
        logger.info("Question with id=%s retrieved successfully with %d answers", id, len(answers))

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
