from dataclasses import dataclass
from src.common.application.query import Query
from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.email import Email
from src.common.domain.value_objects.sex import Sex


@dataclass(frozen=True)
class GetByIdPsychologistQuery(Query[str]):
    cedula: str