from fastapi import APIRouter, HTTPException
from fastapi_injector import Injected
from mediatr import Mediator

from src.common.domain.value_objects.email import Email
from src.modules.users_management.api.auth.login_dto import LoginDto
from src.modules.users_management.application.interactors.login.invalid_credentials_exception import \
    InvalidCredentialsException
from src.modules.users_management.application.interactors.login.login_command import LoginCommand

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(login_dto: LoginDto, mediator: Mediator = Injected(Mediator)):
    command = LoginCommand(
        email=Email(login_dto.email),
        password=login_dto.password,
        role=login_dto.role
    )
    try:
        token = await mediator.send_async(command)
        return {"accessToken": token}
    except InvalidCredentialsException:
        raise HTTPException(status_code=401)
