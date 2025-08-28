from app.application.common.gateway import Gateway


class RemoveQuestionIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> None:
        self._gateway.remove_question(id)
