from dataclasses import dataclass

from src.common.domain.value_objects.sex import Sex


@dataclass(frozen=True)
class GetPsychologistResponse:
    cedula: str
    name: str
    sex: Sex
    email: str
