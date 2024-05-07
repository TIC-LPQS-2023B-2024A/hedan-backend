from datetime import timedelta

from pydantic import BaseModel, field_validator

from src.modules.questionnaires.domain.value_objects.answer import Answer
from src.modules.questionnaires.domain.value_objects.question_id import QuestionId


class RegisterChildResponseAnswerDto(BaseModel):
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


class RegisterChildResponseDto(BaseModel):
    child_cedula: str
    psychologist_cedula: str
    child_age: int
    child_scholar_grade: int
    reason: str
    referrer: str
    answers: list[RegisterChildResponseAnswerDto]

    @field_validator("answers")
    @classmethod
    def validate_answers(cls, v: list[RegisterChildResponseAnswerDto]) -> list[RegisterChildResponseAnswerDto]:
        if len(v) != 49:
            raise ValueError("Answers must be 49")
        return v

    @field_validator("child_age")
    @classmethod
    def validate_child_age(cls, v: int) -> int:
        if v < 6 or v > 8:
            raise ValueError("Child age must be between 6 and 8")
        return v
