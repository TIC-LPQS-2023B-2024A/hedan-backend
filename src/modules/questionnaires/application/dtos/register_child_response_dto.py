from dataclasses import dataclass
from datetime import timedelta

from src.modules.questionnaires.domain.value_objects.answer import Answer
from src.modules.questionnaires.domain.value_objects.question_id import QuestionId


@dataclass(kw_only=True)
class RegisterChildResponseAnswerDto:
    question_id: int
    answer: bool
    time_taken: int


class RegisterChildResponseAnswerDtoMapper:

    @staticmethod
    def to_domain_answer(dto: RegisterChildResponseAnswerDto) -> Answer:
        return Answer(
            question_id=QuestionId(dto.question_id),
            value=dto.answer,
            time_taken=timedelta(milliseconds=dto.time_taken)
        )


@dataclass(kw_only=True)
class RegisterChildResponseDto:
    child_cedula: str
    psychologist_cedula: str
    child_age: int
    child_scholar_grade: int
    reason: str
    referrer: str
    answers: list[RegisterChildResponseAnswerDto]

    def _validate(self):
        self._validate_answers()
        self._validate_child_age()

    def _validate_answers(self):
        if len(self.answers) != 49:
            raise ValueError("Answers must be 49")

    def _validate_child_age(self):
        if self.child_age < 6 or self.child_age > 8:
            raise ValueError("Child age must be between 6 and 8")
