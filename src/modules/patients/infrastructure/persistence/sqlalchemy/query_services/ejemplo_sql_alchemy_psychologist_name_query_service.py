from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.get_psychologist_name_query import \
    GetPsychologistNameQuery
from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.psychologist_name_query_service import \
    PsychologistNameQueryService
from src.modules.patients.infrastructure.persistence.sqlalchemy.models.psychologist_model import PsychologistModel


class SqlAlchemyPsychologistNameQueryService(PsychologistNameQueryService):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def execute_async(self, query: GetPsychologistNameQuery) -> str:
        async with self.__async_session_factory() as session:
            result = select(PsychologistModel.name).where(PsychologistModel.cedula == str(query.cedula)).fetch(1)
            return (await session.execute(result)).scalar()
