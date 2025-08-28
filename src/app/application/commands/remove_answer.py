from app.application.common.gateway import Gateway


class RemoveAnswerIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> None:
        self._gateway.remove_answer(id)
