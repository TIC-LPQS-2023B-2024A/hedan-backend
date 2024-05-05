from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.exc import MissingGreenlet
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.common.domain.value_objects.cedula import Cedula
from src.common.infrastructure.repositories.sqlachemy.base import Base
from src.modules.questionnaires.domain.entities.child import Child
from src.modules.questionnaires.infrastructure.models.sqlachemy.questionnaire_response import \
    QuestionnaireResponseModel, QuestionnaireResponseDataMapper


class ChildModel(Base):
    __tablename__ = "child"
    cedula: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    sex: Mapped[str] = mapped_column(String(1))
    psychologist_id: Mapped[int] = mapped_column(ForeignKey("psychologist.cedula"))
    psychologist: Mapped["PsychologistModel"] = relationship("PsychologistModel", back_populates="children")
    questionnaire_responses: Mapped[List[QuestionnaireResponseModel]] = relationship("QuestionnaireResponseModel",
                                                                                     back_populates="child")


class ChildDataMapper:

    @staticmethod
    def model_to_entity(instance: ChildModel) -> Child:
        child = Child(
            cedula=Cedula(instance.cedula),
            name=instance.name,
            sex=instance.sex,
            psychologist_id=Cedula(instance.psychologist_id)
        )
        try:
            _ = instance.questionnaire_responses
        except MissingGreenlet:
            pass
        else:
            [child.add_questionnaire_response(QuestionnaireResponseDataMapper.model_to_entity(response)) for response
             in instance.questionnaire_responses]
        return child

    @staticmethod
    def entity_to_model(entity: Child) -> ChildModel:
        return ChildModel(
            cedula=entity.cedula,
            name=entity.name,
            sex=str(entity.sex),
            psychologist_id=str(entity.psychologist_id),
            questionnaire_responses=[QuestionnaireResponseDataMapper.entity_to_model(response) for response in
                                     entity.questionnaire_responses]
        )
