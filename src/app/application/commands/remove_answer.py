from app.application.common.gateway import Gateway
from app.domain.entities import Answer


class RemoveAnswerIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> Answer | None:
        return self._gateway.remove_answer(id)
