from fastapi import APIRouter
from fastapi_injector import Injected
from mediatr import Mediator

from src.common.domain.value_objects.cedula import Cedula
from src.modules.patients.api.psychologist.ejemplo_add_child_dto import AddChildDto
from src.modules.patients.application.interactors.ejemplo_add_child.add_child_command import AddChildCommand
from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.get_psychologist_name_query import \
    GetPsychologistNameQuery
from src.modules.patients.domain.child.scholar_grade import ScholarGrade

router = APIRouter(prefix="/psychologists", tags=["Psychologists"])


@router.post("/{psychologist_cedula}/childs")
async def add_child(psychologist_cedula: str, add_child_dto: AddChildDto, mediator: Mediator = Injected(Mediator)):
    command = AddChildCommand(
        name=add_child_dto.name,
        sex=add_child_dto.sex,
        birthdate=add_child_dto.birthdate,
        scholar_grade=ScholarGrade(add_child_dto.scholar_grade),
        psychologist_cedula=Cedula(psychologist_cedula)
    )
    return await mediator.send_async(command)


@router.get("/{psychologist_cedula}/name")
async def get_psychologist_name(psychologist_cedula: str, mediator: Mediator = Injected(Mediator)):
    query = GetPsychologistNameQuery(
        cedula=Cedula(psychologist_cedula)
    )
    return await mediator.send_async(query)

