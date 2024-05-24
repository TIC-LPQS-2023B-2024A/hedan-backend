from dataclasses import dataclass

from src.common.domain.value_object import ValueObject


@dataclass(frozen=True)
class TestResults(ValueObject):
    social_anxiety_index: int
    physiological_anxiety_index: int
    defensiveness_index: int
    worry_index: int
    total_anxiety_index: int
    inconsistent_answers_index: int
