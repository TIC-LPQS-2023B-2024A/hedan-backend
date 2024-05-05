from datetime import timedelta
from dataclasses import dataclass

from src.modules.questionnaires.domain.value_objects.question_id import QuestionId


@dataclass(frozen=True)
class Answer:
    question_id: QuestionId
    value: bool
    time_taken: timedelta

    def __post_init__(self):
        pass

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other
