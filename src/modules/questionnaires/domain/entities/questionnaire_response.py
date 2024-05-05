from datetime import date

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.domain.value_objects.answer import Answer
from src.modules.questionnaires.domain.value_objects.scholar_grade import ScholarGrade


class QuestionnaireResponse:
    def __init__(
            self,
            child_age: int,
            child_scholar_grade: ScholarGrade,
            reason: str,
            referrer: str,
            psychologist_id: Cedula,
            child_id: Cedula,
            answers: tuple[Answer, ...] = (),
            id: int = None,
            date_taken: date = date.today()
    ):
        self.id = id
        self.child_age = child_age
        self.child_scholar_grade = child_scholar_grade
        self.date = date_taken
        self.reason = reason
        self.referrer = referrer
        self.psychologist_id = psychologist_id
        self.child_id = child_id
        self.answers = answers

    def __post_init__(self):
        self._validate()

    def _validate(self):
        self._validate_answers()
        self._validate_child_age()

    def _validate_answers(self):
        if len(self.answers) != 49:
            raise ValueError("Answers must be 49")

    def _validate_child_age(self):
        if self.child_age < 6 or self.child_age > 8:
            raise ValueError("Child age must be between 6 and 8")

    def __eq__(self, other):
        return self.id == other.id
