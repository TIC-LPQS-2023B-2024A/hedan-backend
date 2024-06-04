from injector import Inject
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.domain.value_objects.cedula import Cedula
from src.modules.patients.domain.psychologist.psychologist import Psychologist
from src.modules.patients.domain.psychologist.psychologist_repository_async import PsychologistRepositoryAsync
from src.modules.patients.infrastructure.persistence.sqlalchemy.models.psychologist_model import PsychologistModel


class SqlAlchemyPsychologistRepositoryAsync(PsychologistRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def add_psychologist(self, psychologist: Psychologist) -> Cedula:
        psychologist_model = PsychologistModel(
            cedula=str(psychologist.id),
            name=psychologist.name,
            sex=psychologist.sex,
            email=str(psychologist.email)
        )
        async with self.__async_session_factory() as session:
            session.add(psychologist_model)
            await session.commit()

        return psychologist.id
