from abc import ABC, abstractmethod
from typing import Optional

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse


class AbstractQuestionnaireResponsesRepositoryAsync(ABC):
    @abstractmethod
    async def register_psychologist_child_questionnaire_response_async(
            self,
            psychologist_cedula: Cedula,
            child_cedula: Cedula,
            questionnaire_response: QuestionnaireResponse
    ) -> QuestionnaireResponse:
        pass

    @abstractmethod
    async def get_by_id_async(self, id: int) -> Optional[QuestionnaireResponse]:
        pass
