import logging

from app.application.common.gateway import Gateway
from app.domain.entities import Question

logger = logging.getLogger(__name__)


class RemoveQuestionInteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> Question | None:
        logger.info("Request to remove question with id=%s", id)
        return self._gateway.remove_question(id)
