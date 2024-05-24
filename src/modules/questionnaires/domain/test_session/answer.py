from datetime import timedelta
from dataclasses import dataclass

from src.common.domain.value_object import ValueObject
from src.modules.questionnaires.domain.test_session.question_id import QuestionId


@dataclass(frozen=True)
class Answer(ValueObject):
    question_id: QuestionId
    value: bool
    time_taken: timedelta

    def __post_init__(self):
        pass

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other
