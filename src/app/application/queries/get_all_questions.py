from app.application.common.dto import QuestionResponse
from app.application.common.gateway import Gateway


class GetAllQuestionsIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self) -> list[QuestionResponse]:
        questions = self._gateway.get_all_questions()
        return [
            QuestionResponse(id=q.id, text=q.text, created_at=q.created_at)
            for q in questions
        ]
