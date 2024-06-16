from fastapi import APIRouter
from fastapi_injector import Injected
from mediatr import Mediator

from src.common.domain.value_objects.cedula import Cedula
from src.modules.patients.api.psychologist.add_child_dto import AddChildDto
from src.modules.patients.application.interactors.add_child.add_child_command import AddChildCommand
from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.get_psychologist_name_query import \
    GetPsychologistNameQuery
from src.modules.patients.application.interactors.get_children.get_children_query import GetChildrenQuery
from src.modules.patients.domain.child.scholar_grade import ScholarGrade

router = APIRouter(prefix="/psychologists", tags=["Psychologists"])


@router.post("/{psychologist_cedula}/add_child")
async def add_child(psychologist_cedula: str, add_child_dto: AddChildDto, mediator: Mediator = Injected(Mediator)):
    command = AddChildCommand(
        name=add_child_dto.name,
        sex=add_child_dto.sex,
        birthdate=add_child_dto.birthdate,
        scholar_grade=ScholarGrade(add_child_dto.scholar_grade),
        test_sender=add_child_dto.test_sender,
        test_reason=add_child_dto.test_reason,
        psychologist_cedula=Cedula(psychologist_cedula)
    )
    return await mediator.send_async(command)


@router.get("/{psychologist_cedula}/name")
async def get_psychologist_name(psychologist_cedula: str, mediator: Mediator = Injected(Mediator)):
    query = GetPsychologistNameQuery(
        cedula=Cedula(psychologist_cedula)
    )
    return await mediator.send_async(query)


@router.get("/{psychologist_cedula}/children")
async def get_children(psychologist_cedula: str, mediator: Mediator = Injected(Mediator)):
    query = GetChildrenQuery(
        cedula=Cedula(psychologist_cedula)
    )
    return await mediator.send_async(query)

