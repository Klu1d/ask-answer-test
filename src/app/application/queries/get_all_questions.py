import logging
from app.application.common.dto import QuestionResponse
from app.application.common.gateway import Gateway

logger = logging.getLogger(__name__)

class GetAllQuestionsInteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self) -> list[QuestionResponse]:
        logger.info("Request to get all questions")
        questions = self._gateway.get_all_questions()
        logger.info("Retrieved %d questions", len(questions))
        return [
            QuestionResponse(id=q.id, text=q.text, created_at=q.created_at)
            for q in questions
        ]
