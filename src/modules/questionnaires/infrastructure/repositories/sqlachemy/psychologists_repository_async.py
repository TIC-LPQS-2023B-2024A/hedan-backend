from typing import Optional

from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.application.interfaces.repositories.psychologists_repository_async import \
    AbstractPsychologistsRepositoryAsync as IPsychologistsRepositoryAsync
from src.modules.questionnaires.domain.entities.psychologist import Psychologist
from src.modules.questionnaires.infrastructure.models.sqlachemy.psychologist import PsychologistModel, \
    PsychologistDataMapper


class PsychologistsRepositoryAsync(IPsychologistsRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def get_by_id_async(self, psychologist_cedula: Cedula) -> Optional[Psychologist]:
        async with self.__async_session_factory() as session:
            statement = await session.execute(
                select(PsychologistModel).where(PsychologistModel.cedula == str(psychologist_cedula))
            )
            result = statement.scalars().first()
            return None if result is None else PsychologistDataMapper.model_to_entity(result)
