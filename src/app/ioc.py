from typing import Iterable

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.orm import Session, sessionmaker

from app.application.common.gateway import Gateway
from app.application.commands import (
    CreateAnswerIteractor,
    CreateQuestionIteractor,
    RemoveAnswerIteractor,
    RemoveQuestionIteractor,
)
from app.application.queries import (
    GetAllQuestionsIteractor,
    GetAnswerIteractor,
    GetQuestionIteractor,
)
from app.infrastructure.common.gateway import SQLAlchemyGateway
from app.infrastructure.persistence.config import Config
from app.infrastructure.persistence.providers import get_sessionmaker


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> sessionmaker[Session]:
        return get_sessionmaker(config.postgres)

    @provide(scope=Scope.REQUEST)
    def get_session(self, session_maker: sessionmaker[Session]) -> Iterable[Session]:
        with session_maker() as session:
            yield session

    gateway = provide(SQLAlchemyGateway, provides=Gateway, scope=Scope.REQUEST)

    create_answer_iteractor = provide(CreateAnswerIteractor, scope=Scope.REQUEST)
    create_question_iteractor = provide(CreateQuestionIteractor, scope=Scope.REQUEST)
    remove_iteractor_ = provide(RemoveAnswerIteractor, scope=Scope.REQUEST)
    remove_question_iteractor_ = provide(RemoveQuestionIteractor, scope=Scope.REQUEST)
    get_all_questions_iteractor = provide(GetAllQuestionsIteractor, scope=Scope.REQUEST)
    get_answers_iteractor = provide(GetAnswerIteractor, scope=Scope.REQUEST)
    get_question_iteractor = provide(GetQuestionIteractor, scope=Scope.REQUEST)
