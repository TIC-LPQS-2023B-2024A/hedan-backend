from fastapi_injector import request_scope
from injector import Injector, singleton
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.infrastructure.repositories.sqlachemy.db import create_async_session
# Repositories Interfaces
from src.modules.questionnaires.application.interfaces.repositories.children_repository_async import \
    ChildrenRepositoryAsync as IChildrenRepositoryAsync
from src.modules.questionnaires.application.interfaces.repositories.psychologists_repository_async import \
    PsychologistsRepositoryAsync as IPsychologistsRepositoryAsync
from src.modules.questionnaires.application.interfaces.repositories.questionnaire_responses_repository_async import \
    QuestionnaireResponsesRepositoryAsync as IQuestionnaireResponsesRepositoryAsync
# Services
from src.modules.questionnaires.application.services.child_questionnaire_responses_service import \
    ChildQuestionnaireResponsesService
# Helpers Interfaces
# ---
# Repositories Implementations
from src.modules.questionnaires.infrastructure.repositories.sqlachemy.children_repository_async import \
    ChildrenRepositoryAsync as SqlAlchemyChildrenRepositoryAsync
from src.modules.questionnaires.infrastructure.repositories.sqlachemy.psychologists_repository_async import \
    PsychologistsRepositoryAsync as SqlAlchemyPsychologistsRepositoryAsync
from src.modules.questionnaires.infrastructure.repositories.sqlachemy.questionnaire_response_repository_async import \
    QuestionnaireResponseRepositoryAsync as SqlAlchemyQuestionnaireResponseRepositoryAsync


# Helpers Implementations
# ---


def add_database(injector: Injector) -> Injector:
    injector.binder.bind(async_sessionmaker[AsyncSession], to=create_async_session, scope=singleton)
    return injector


def add_repositories(injector: Injector) -> Injector:
    injector.binder.bind(IChildrenRepositoryAsync, to=SqlAlchemyChildrenRepositoryAsync, scope=request_scope)
    injector.binder.bind(IQuestionnaireResponsesRepositoryAsync, to=SqlAlchemyQuestionnaireResponseRepositoryAsync,
                         scope=request_scope)
    injector.binder.bind(IPsychologistsRepositoryAsync, to=SqlAlchemyPsychologistsRepositoryAsync, scope=request_scope)
    return injector


def add_helpers(injector: Injector) -> Injector:
    return injector


def add_services(injector: Injector) -> Injector:
    injector.binder.bind(ChildQuestionnaireResponsesService, to=ChildQuestionnaireResponsesService, scope=request_scope)
    return injector


def add_dependencies(injector: Injector) -> Injector:
    injector = add_database(injector)
    injector = add_repositories(injector)
    injector = add_helpers(injector)
    injector = add_services(injector)
    return injector
