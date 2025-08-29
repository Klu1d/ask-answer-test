from app.application.common.gateway import Gateway
from app.domain.entities import Question


class RemoveQuestionIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> Question | None:
        return self._gateway.remove_question(id)
