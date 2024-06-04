from fastapi import APIRouter, Security
from fastapi_injector import Injected
from fastapi_jwt import JwtAuthorizationCredentials
from mediatr import Mediator
from starlette import status

from src.common.api.authorization import admin_only_async
from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.email import Email
from src.common.infrastructure.token.access_security import access_security
from src.modules.users_management.api.users.add_psychologist_user_dto import AddPsychologistUserDto
from src.modules.users_management.application.interactors.add_psychologist_user.add_psychologist_user_command import \
    AddPsychologistUserCommand

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/psychologists", status_code=status.HTTP_201_CREATED)
@admin_only_async
async def add_psychologist_user(
        add_psychologist_user_dto: AddPsychologistUserDto,
        mediator: Mediator = Injected(Mediator),
        credentials: JwtAuthorizationCredentials = Security(access_security)
):
    command = AddPsychologistUserCommand(
        cedula=Cedula(add_psychologist_user_dto.cedula),
        name=add_psychologist_user_dto.name,
        sex=add_psychologist_user_dto.sex,
        email=Email(add_psychologist_user_dto.email),
        password=add_psychologist_user_dto.password
    )
    await mediator.send_async(command)
