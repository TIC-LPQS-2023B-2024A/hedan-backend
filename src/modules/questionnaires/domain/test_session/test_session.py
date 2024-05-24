from datetime import datetime
from typing import Optional

from src.common.domain.aggregate_root import AggregateRoot
from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.domain.test_session.answers_set import AnswerSet
from src.modules.questionnaires.domain.test_session.cmasr2_calculator import calculate_cmasr2_test_results
from src.modules.questionnaires.domain.test_session.test_results import TestResults


class TestSession(AggregateRoot[int]):
    def __init__(
            self,
            id: int,
            child_id: int,
            psychologist_cedula: Cedula,
            child_age: int,
            scholar_grade: int
    ):
        self.__id = id
        self.__child_id = child_id
        self.__psychologist_cedula = psychologist_cedula
        self.__child_age = child_age
        self.__scholar_grade = scholar_grade
        self.__date_time_of_answer: Optional[datetime] = None
        self.__answer_set: Optional[AnswerSet] = None
        self.__test_results: Optional[TestResults] = None

    @property
    def id(self):
        return self.__id

    @property
    def child_id(self):
        return self.__child_id

    @property
    def psychologist_cedula(self):
        return self.__psychologist_cedula

    @property
    def child_age(self):
        return self.__child_age

    @property
    def scholar_grade(self):
        return self.__scholar_grade

    @property
    def date_time_of_answer(self):
        return self.__date_time_of_answer

    @property
    def answer_set(self):
        return self.__answer_set

    @property
    def test_results(self):
        return self.__test_results

    @answer_set.setter
    def answer_set(self, answer_set: AnswerSet):
        self.__date_time_of_answer = datetime.now()
        self.__answer_set = answer_set
        self.__calculate_test_results()

    def __calculate_test_results(self):
        if self.answer_set is None:
            raise ValueError("The answer set is not set")
        else:
            return calculate_cmasr2_test_results(self.answer_set)
