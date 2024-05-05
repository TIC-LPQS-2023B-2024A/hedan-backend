from typing import Optional

from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.application.interfaces.repositories.questionnaire_responses_repository_async import \
    AbstractQuestionnaireResponsesRepositoryAsync as IQuestionnaireResponseRepositoryAsync
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse
from src.modules.questionnaires.infrastructure.models.sqlachemy.questionnaire_response import \
    QuestionnaireResponseModel, QuestionnaireResponseDataMapper


class QuestionnaireResponseRepositoryAsync(IQuestionnaireResponseRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def register_psychologist_child_questionnaire_response_async(
            self, psychologist_cedula: Cedula,
            child_cedula: Cedula,
            questionnaire_response: QuestionnaireResponse
    ) -> QuestionnaireResponse:
        async with self.__async_session_factory() as session:
            questionnaire_response_model = QuestionnaireResponseDataMapper.entity_to_model(questionnaire_response)
            session.add(questionnaire_response_model)
            await session.commit()
            return QuestionnaireResponseDataMapper.model_to_entity(questionnaire_response_model)

    async def get_by_id_async(self, id: int) -> Optional[QuestionnaireResponse]:
        async with self.__async_session_factory() as session:
            statement = await session.execute(
                select(QuestionnaireResponseModel).where(QuestionnaireResponseModel.id == id)
            )
            result = statement.scalars().first()
            return None if result is None else QuestionnaireResponseDataMapper.model_to_entity(result)
