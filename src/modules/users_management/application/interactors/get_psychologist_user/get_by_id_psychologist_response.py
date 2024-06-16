from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.email import Email
from src.common.domain.value_objects.sex import Sex


@dataclass(frozen=True)
class GetByIdPsychologistResponse:

    cedula: str
    name: str
    sex: Sex
    email: str

