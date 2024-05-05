import copy

from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.sex import Sex
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse


class Child:
    def __init__(
            self, cedula: Cedula,
            name: str,
            sex: Sex,
            psychologist_id: Cedula
    ):
        self.cedula = cedula
        self.name = name
        self.sex = sex
        self.psychologist_id = psychologist_id
        self.__questionnaire_responses: list[QuestionnaireResponse] = []

    @property
    def questionnaire_responses(self) -> tuple[QuestionnaireResponse, ...]:
        return tuple(copy.deepcopy(self.__questionnaire_responses))

    def add_questionnaire_response(self, questionnaire_response: QuestionnaireResponse):
        self.__questionnaire_responses.append(questionnaire_response)

    def __eq__(self, other):
        return self.cedula == other.cedula
