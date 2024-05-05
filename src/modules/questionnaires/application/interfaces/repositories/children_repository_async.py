from abc import ABC, abstractmethod
from typing import Optional

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.domain.entities.child import Child


class ChildrenRepositoryAsync(ABC):
    @abstractmethod
    async def get_by_id_async(self, child_cedula: Cedula) -> Optional[Child]:
        pass
