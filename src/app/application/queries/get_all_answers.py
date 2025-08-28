from app.application.common.gateway import Gateway
from app.application.common.dto import QuestionResponse, AnswerResponse


class GetAllAnswersIteractor:
    def __init__(self, gateway: Gateway):
        self._gateway = gateway

    def execute(self, id: int) -> dict[QuestionResponse, list[AnswerResponse]]:
        question, answers = self._gateway.get_question(id)
        return {
            "question": QuestionResponse(
                id=question.id,
                text=question.text,
                created_at=question.created_at
            ),
            "answers": [
                AnswerResponse(
                    id=a.id,
                    text=a.text,
                    user_id=a.user_id,
                    question_id=a.question_id,
                    created_at=a.created_at,
                )
                for a in answers
            ]
        }
        
