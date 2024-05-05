from typing import Optional

from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.application.interfaces.repositories.children_repository_async import \
    AbstractChildrenRepositoryAsync
from src.modules.questionnaires.domain.entities.child import Child
from src.modules.questionnaires.infrastructure.models.sqlachemy.child import ChildModel, ChildDataMapper


class ChildrenRepositoryAsync(AbstractChildrenRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def get_by_id_async(self, child_cedula: Cedula) -> Optional[Child]:
        async with self.__async_session_factory() as session:
            statement = await session.execute(
                select(ChildModel).where(ChildModel.cedula == str(child_cedula))
            )
            result = statement.scalars().first()
            return None if result is None else ChildDataMapper.model_to_entity(result)
