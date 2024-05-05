from abc import ABC, abstractmethod
from typing import Optional

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.domain.entities.psychologist import Psychologist


class AbstractPsychologistsRepositoryAsync(ABC):
    @abstractmethod
    async def get_by_id_async(self, psychologist_cedula: Cedula) -> Optional[Psychologist]:
        pass
