import copy

from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.sex import Sex
from src.modules.questionnaires.domain.entities.child import Child
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse


class Psychologist:
    def __init__(self, cedula: Cedula, name: str, sex: Sex) -> None:
        self.cedula = cedula
        self.name = name
        self.sex = sex
        self.__children: list[Child] = []
        self.__questionnaire_responses: list[QuestionnaireResponse] = []

    @property
    def children(self) -> tuple[Child, ...]:
        return tuple(copy.deepcopy(self.__children))

    def add_child(self, child: Child) -> None:
        self.__children.append(child)

    @property
    def questionnaire_responses(self) -> tuple[QuestionnaireResponse, ...]:
        return tuple(copy.deepcopy(self.__questionnaire_responses))

    def add_questionnaire_response(self, questionnaire_response):
        self.__questionnaire_responses.append(questionnaire_response)

    def __eq__(self, other):
        return self.cedula == other.cedula
