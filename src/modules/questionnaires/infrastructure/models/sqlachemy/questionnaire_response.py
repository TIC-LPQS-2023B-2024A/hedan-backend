from datetime import date, timedelta

from sqlalchemy import ForeignKey, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.common.domain.value_objects.cedula import Cedula
from src.common.infrastructure.repositories.sqlachemy.base import Base
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse
from src.modules.questionnaires.domain.value_objects.answer import Answer
from src.modules.questionnaires.domain.value_objects.question_id import QuestionId
from src.modules.questionnaires.domain.value_objects.scholar_grade import ScholarGrade


class QuestionnaireResponseModel(Base):
    __tablename__ = "questionnaire_response"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    child_age: Mapped[int] = mapped_column(Integer)
    child_scholar_grade: Mapped[int] = mapped_column(Integer)
    date: Mapped[date] = mapped_column(Date)
    reason: Mapped[str] = mapped_column(String(170))
    referrer: Mapped[str] = mapped_column(String(50))
    answers: Mapped[list[dict]] = mapped_column(JSONB, default=[])
    psychologist_id: Mapped[int] = mapped_column(ForeignKey("psychologist.cedula"))
    psychologist: Mapped["PsychologistModel"] = relationship("PsychologistModel",
                                                             back_populates="questionnaire_responses")
    child_id: Mapped[int] = mapped_column(ForeignKey("child.cedula"))
    child: Mapped["ChildModel"] = relationship("ChildModel",
                                               back_populates="questionnaire_responses")


class QuestionnaireResponseDataMapper:
    @staticmethod
    def model_to_entity(instance: QuestionnaireResponseModel) -> QuestionnaireResponse:
        return QuestionnaireResponse(
            id=instance.id,
            child_age=instance.child_age,
            child_scholar_grade=ScholarGrade(instance.child_scholar_grade),
            reason=instance.reason,
            referrer=instance.referrer,
            child_id=Cedula(instance.child_id),
            psychologist_id=Cedula(instance.psychologist_id),
            date_taken=instance.date,
            answers=tuple([QuestionnaireResponseDataMapper.jsonb_dict_to_answer(
                answer
            ) for answer in instance.answers])
        )

    @staticmethod
    def entity_to_model(entity: QuestionnaireResponse) -> QuestionnaireResponseModel:
        return QuestionnaireResponseModel(
            id=entity.id,
            child_age=entity.child_age,
            child_scholar_grade=entity.child_scholar_grade.value,
            reason=entity.reason,
            referrer=entity.referrer,
            psychologist_id=str(entity.psychologist_id),
            child_id=str(entity.child_id),
            date=entity.date,
            answers=[QuestionnaireResponseDataMapper.answer_to_jsonb_dict(answer) for answer in entity.answers]
        )

    @staticmethod
    def answer_to_jsonb_dict(answer: Answer) -> dict:
        return {
            'questionId': int(answer.question_id),
            'answer': answer.value,
            'timeTaken': answer.time_taken.microseconds // 1000
        }

    @staticmethod
    def jsonb_dict_to_answer(jsonb: dict) -> Answer:
        return Answer(
            question_id=QuestionId(jsonb['questionId']),
            value=jsonb['answer'],
            time_taken=timedelta(milliseconds=jsonb['timeTaken'])
        )
