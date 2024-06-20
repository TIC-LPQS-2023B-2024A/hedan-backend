from injector import Inject
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.modules.results_analysis.domain.test_report.test_report import TestReport
from src.modules.results_analysis.domain.test_report.test_report_repository_async import TestReportRepositoryAsync
from src.modules.results_analysis.infrastructure.persistence.sqlalchemy.models.test_report_model import TestReportModel


class SqlAlchemyTestReportRepositoryAsync(TestReportRepositoryAsync):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def add_test_report(self, test_report: TestReport):
        test_report_model = TestReportModel(
            child_id=test_report.child_id,
            test_session_id=test_report.test_session_id,
            psychologist_cedula=str(test_report.psychologist_cedula),
            child_age=test_report.child_age,
            scholar_grade=test_report.scholar_grade,
            child_sex=str(test_report.child_sex),
            date_time_of_answer=test_report.date_time_of_answer,
            test_results=test_report.test_results.to_dict(),
            time_taken=int(test_report.time_taken.total_seconds() * 1000)
        )
        async with self.__async_session_factory() as session:
            session.add(test_report_model)
            await session.commit()
