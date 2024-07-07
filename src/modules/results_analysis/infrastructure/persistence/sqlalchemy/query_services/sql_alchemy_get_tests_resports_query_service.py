from typing import Optional

from injector import Inject
from sqlalchemy import select, Sequence, Row
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.modules.patients.application.interactors.get_children.get_children_query import GetChildrenQuery
from src.modules.patients.application.interactors.get_children.get_children_query_service import ChildrenQueryService
from src.modules.patients.infrastructure.persistence.sqlalchemy.models.child_model import ChildModel
from src.modules.patients.infrastructure.persistence.sqlalchemy.models.psychologist_model import PsychologistModel
from src.modules.results_analysis.application.interactors.get_test_response.get_tests_reports_query import \
    GetTestsReportsQuery
from src.modules.results_analysis.infrastructure.persistence.sqlalchemy.models.test_report_model import TestReportModel


class GetTestsReportsQueryService:
    pass


class SqlAlchemyGetTestsReportsQueryService(GetTestsReportsQueryService):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def execute_async(self, query: GetTestsReportsQuery) -> Optional[list[TestReportModel]]:
        async with self.__async_session_factory() as session:
            query = select(TestReportModel).where(TestReportModel.psychologist_cedula == str(query.psychologist_cedula))
            result = (await session.execute(query)).scalars().all()
            test_reports: list[TestReportModel] = []
            for testReport in result:
                test_reports.append(TestReportModel(
                    id=testReport.id,
                    child_id=testReport.child_id,
                    psychologist_cedula=testReport.psychologist_cedula,
                    test_session_id=testReport.test_session_id,
                    child_age=testReport.child_age,
                    scholar_grade=testReport.scholar_grade,
                    child_sex=testReport.child_sex,
                    date_time_of_answer=testReport.date_time_of_answer,
                    test_results=testReport.test_results,
                    time_taken=testReport.time_taken
                    )
                )

            if result is None:
                return None

            return test_reports

