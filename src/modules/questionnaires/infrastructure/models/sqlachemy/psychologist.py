from typing import List

from sqlalchemy import String
from sqlalchemy.exc import MissingGreenlet
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.common.domain.value_objects.cedula import Cedula
from src.common.infrastructure.repositories.sqlachemy.base import Base
from src.modules.questionnaires.domain.entities.psychologist import Psychologist
from src.modules.questionnaires.infrastructure.models.sqlachemy.child import ChildModel, ChildDataMapper
from src.modules.questionnaires.infrastructure.models.sqlachemy.questionnaire_response import \
    QuestionnaireResponseModel, QuestionnaireResponseDataMapper


class PsychologistModel(Base):
    __tablename__ = "psychologist"
    cedula: Mapped[str] = mapped_column(String(10), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    sex: Mapped[str] = mapped_column(String(1))
    children: Mapped[List[ChildModel]] = relationship("ChildModel", back_populates="psychologist")
    questionnaire_responses: Mapped[List[QuestionnaireResponseModel]] = relationship("QuestionnaireResponseModel",
                                                                                     back_populates="psychologist")


class PsychologistDataMapper:
    @staticmethod
    def model_to_entity(instance: PsychologistModel) -> Psychologist:
        psychologist = Psychologist(
            cedula=Cedula(instance.cedula),
            name=instance.name,
            sex=instance.sex
        )
        try:
            _ = instance.children
        except MissingGreenlet:
            pass
        else:
            [psychologist.add_child(ChildDataMapper.model_to_entity(child)) for child in instance.children]

        try:
            _ = instance.questionnaire_responses
        except MissingGreenlet:
            pass
        else:
            if hasattr(instance, 'questionnaire_responses'):
                [psychologist.add_questionnaire_response(QuestionnaireResponseDataMapper.model_to_entity(response))
                 for response in instance.questionnaire_responses]

        return psychologist

    @staticmethod
    def entity_to_model(entity: Psychologist) -> PsychologistModel:
        return PsychologistModel(
            cedula=str(entity.cedula),
            name=entity.name,
            sex=entity.sex,
            children=[ChildDataMapper.entity_to_model(child) for child in entity.children],
            questionnaire_responses=[QuestionnaireResponseDataMapper.entity_to_model(response) for response
                                     in entity.questionnaire_responses]
        )
