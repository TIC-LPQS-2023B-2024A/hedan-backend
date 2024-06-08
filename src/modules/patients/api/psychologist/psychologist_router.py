from typing import List

from fastapi import APIRouter, Security
from fastapi_injector import Injected
from fastapi_jwt import JwtAuthorizationCredentials
from mediatr import Mediator

from src.common.api.authorization import admin_only
from src.common.infrastructure.token.access_security import access_security
from src.modules.patients.api.psychologist.psychologist_dto import PsychologistDto
from src.modules.patients.application.interactors.get_psychologists.get_psychologist_list_query import \
    GetPsychologistListQuery
from src.modules.patients.application.interactors.get_psychologists.get_psychologist_response import \
    GetPsychologistListResponse
from src.modules.patients.domain.psychologist.psychologist import Psychologist

router = APIRouter(prefix="/psychologists", tags=["psychologists"], dependencies=[Security(access_security), Security(admin_only)])


@router.get("/all", response_model=List[GetPsychologistListResponse])
async def get_psychologists(
        mediator: Mediator = Injected(Mediator),
) -> List[PsychologistDto]:
    query = GetPsychologistListQuery()
    return await mediator.send_async(query)