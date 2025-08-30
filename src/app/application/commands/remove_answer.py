import logging

from app.application.common.gateway import Gateway
from app.domain.entities import Answer

logger = logging.getLogger(__name__)

class RemoveAnswerInteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> Answer | None:
        logger.info("Request to remove answer with id=%s", id)
        return self._gateway.remove_answer(id)
