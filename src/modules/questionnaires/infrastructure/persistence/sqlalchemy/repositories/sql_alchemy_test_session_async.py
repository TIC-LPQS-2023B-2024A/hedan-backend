from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.sex import Sex
from src.modules.questionnaires.domain.test_session.answers_set import AnswerSet
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
            child_sex=test_session.child_sex,
            test_sender=test_session.test_sender,
            test_reason=test_session.test_reason
        )

        async with self.__async_session_factory() as session:
            session.add(test_model)
            await session.commit()
            return test_model.id

    async def set_answers_set(self, test_session_id: int, answer_set: AnswerSet) -> TestSession:
        async with self.__async_session_factory() as session:
            query = select(TestSessionModel).where(TestSessionModel.id == test_session_id)
            result = await session.execute(query)
            test_session_model = result.scalars().first()
            if test_session_model is None:
                raise ValueError(f"Test session with id {test_session_id} does not exist.")

            test_session = TestSession(
                id=test_session_model.id,
                child_id=test_session_model.child_id,
                psychologist_cedula=Cedula(test_session_model.psychologist_cedula),
                child_age=test_session_model.child_age,
                scholar_grade=test_session_model.scholar_grade,
                child_sex=test_session_model.child_sex,
                test_sender=test_session_model.test_sender,
                test_reason=test_session_model.test_reason
            )
            test_session.answer_set = answer_set

            test_session_model.date_time_of_answer = test_session.date_time_of_answer
            test_session_model.answers = [answer.to_dict() for answer in test_session.answer_set.answer_list]
            test_session_model.test_results = test_session.test_results.to_dict()
            test_session_model.calculate_test_results_timestamp = test_session.calculate_test_results_timestamp

            await session.commit()
            return test_session
