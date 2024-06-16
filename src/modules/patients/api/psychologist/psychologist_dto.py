from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from src.common.application.user_role import UserRole
from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.sex import Sex


class PsychologistDto(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    cedula: Cedula
    name: str
    sex: Sex
    email: str
