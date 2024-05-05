from fastapi import APIRouter
from fastapi_injector import Injected

from src.modules.questionnaires.application.dtos.register_child_response_dto import RegisterChildResponseDto
from src.modules.questionnaires.application.services.child_questionnaire_responses_service import \
    ChildQuestionnaireResponsesService

questionnaire_response_router = APIRouter(prefix="/questionnaire-responses")


@questionnaire_response_router.post("/", response_model=RegisterChildResponseDto)
async def create_questionnaire_response(
        request: RegisterChildResponseDto,
        child_questionnaire_responses_service: ChildQuestionnaireResponsesService = Injected(
            ChildQuestionnaireResponsesService
        )
):
    return await child_questionnaire_responses_service.register_child_response(request)
