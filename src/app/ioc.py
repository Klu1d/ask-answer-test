from typing import Iterable

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.orm import Session, sessionmaker

from app.application.common.gateway import Gateway
from app.application.commands import (
    CreateAnswerInteractor,
    CreateQuestionInteractor,
    RemoveAnswerInteractor,
    RemoveQuestionInteractor,
)
from app.application.queries import (
    GetAllQuestionsInteractor,
    GetAnswerInteractor,
    GetQuestionInteractor,
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

    create_answer_Interactor = provide(CreateAnswerInteractor, scope=Scope.REQUEST)
    create_question_Interactor = provide(CreateQuestionInteractor, scope=Scope.REQUEST)
    remove_Interactor_ = provide(RemoveAnswerInteractor, scope=Scope.REQUEST)
    remove_question_Interactor_ = provide(RemoveQuestionInteractor, scope=Scope.REQUEST)
    get_all_questions_Interactor = provide(GetAllQuestionsInteractor, scope=Scope.REQUEST)
    get_answers_Interactor = provide(GetAnswerInteractor, scope=Scope.REQUEST)
    get_question_Interactor = provide(GetQuestionInteractor, scope=Scope.REQUEST)
