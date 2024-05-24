from datetime import datetime

from src.common.domain.aggregate_root import AggregateRoot
from src.common.domain.value_objects.cedula import Cedula
from src.modules.results_analysis.domain.test_report.test_results import TestResults


class TestReport(AggregateRoot[int]):
    def __init__(
            self,
            id: int,
            child_id: int,
            test_session_id: int,
            psychologist_cedula: Cedula,
            child_age: int,
            scholar_grade: int,
            date_time_of_answer: datetime,
            test_results: TestResults
    ):
        self.__id = id
        self.__child_id = child_id
        self.__psychologist_cedula = psychologist_cedula
        self.__child_age = child_age
        self.__test_session_id = test_session_id
        self.__scholar_grade = scholar_grade
        self.__date_time_of_answer = date_time_of_answer
        self.__test_results = test_results

    @property
    def id(self) -> int:
        return self.__id

    @property
    def child_id(self) -> int:
        return self.__child_id

    @property
    def psychologist_cedula(self) -> Cedula:
        return self.__psychologist_cedula

    @property
    def child_age(self) -> int:
        return self.__child_age

    @property
    def test_session_id(self) -> int:
        return self.__test_session_id

    @property
    def scholar_grade(self) -> int:
        return self.__scholar_grade

    @property
    def date_time_of_answer(self) -> datetime:
        return self.__date_time_of_answer

    @property
    def test_results(self) -> TestResults:
        return self.__test_results
