from typing import List

from fastapi import APIRouter, Security
from fastapi_injector import Injected
from fastapi_jwt import JwtAuthorizationCredentials
from mediatr import Mediator

from src.common.api.authorization import admin_only_async
from src.common.infrastructure.token.access_security import access_security
from src.modules.patients.application.interactors.get_psychologists.get_psychologist_response import \
    GetPsychologistResponse

router = APIRouter(prefix="/psychologists", tags=["psychologists"])


@router.get("/")
@admin_only_async
async def get_psychologists(
        mediator: Mediator = Injected(Mediator),
        credentials: JwtAuthorizationCredentials = Security(access_security)
) -> List[GetPsychologistResponse]:
    #TODO: Implementar listado de psicólogos
    return []
    pass
