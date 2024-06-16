from injector import Inject
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.modules.questionnaires.domain.test_session.test_session import TestSession
from src.modules.questionnaires.domain.test_session.test_session_repository_async import TestSessionRepositoryAsync
from src.modules.questionnaires.infrastructure.persistence.sqlalchemy.models.test_session_model import TestSessionModel


class SqlAlchemyTestSessionRepositoryAsync(TestSessionRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def add_test_session(self, test_session: TestSession) -> int:
        test_model = TestSessionModel(
            child_id=test_session.child_id,
            psychologist_cedula=str(test_session.psychologist_cedula),
            child_age=test_session.child_age,
            scholar_grade=test_session.scholar_grade,
            test_sender=test_session.test_sender,
            test_reason=test_session.test_reason
        )

        async with self.__async_session_factory() as session:
            session.add(test_model)
            await session.commit()
            return test_model.id
