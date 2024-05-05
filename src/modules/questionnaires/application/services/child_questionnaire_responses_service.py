from injector import Inject

from src.common.domain.value_objects.cedula import Cedula
from src.modules.questionnaires.application.dtos.register_child_response_dto import RegisterChildResponseDto, \
    RegisterChildResponseAnswerDtoMapper
from src.modules.questionnaires.application.interfaces.repositories.children_repository_async import \
    AbstractChildrenRepositoryAsync
from src.modules.questionnaires.application.interfaces.repositories.psychologists_repository_async import \
    AbstractPsychologistsRepositoryAsync
from src.modules.questionnaires.application.interfaces.repositories.questionnaire_responses_repository_async import \
    AbstractQuestionnaireResponsesRepositoryAsync
from src.modules.questionnaires.domain.services.questionnaires_service import QuestionnairesService


class ChildQuestionnaireResponsesService:
    def __init__(
            self,
            psychologist_repository: Inject[AbstractPsychologistsRepositoryAsync],
            children_repository: Inject[AbstractChildrenRepositoryAsync],
            questionnaire_responses_repository: Inject[AbstractQuestionnaireResponsesRepositoryAsync]
    ):
        self.__psychologist_repository = psychologist_repository
        self.__children_repository = children_repository
        self.__questionnaire_responses_repository = questionnaire_responses_repository

    async def register_child_response(
            self,
            register_child_response_dto: RegisterChildResponseDto
    ) -> RegisterChildResponseDto:
        psychologist = await self.__psychologist_repository.get_by_id_async(
            Cedula(register_child_response_dto.psychologist_cedula))
        child = await self.__children_repository.get_by_id_async(Cedula(register_child_response_dto.child_cedula))

        QuestionnairesService.register_child_questionnaire_response_by_psychologist(
            child=child,
            psychologist=psychologist,
            child_age=register_child_response_dto.child_age,
            child_scholar_grade=register_child_response_dto.child_scholar_grade,
            reason=register_child_response_dto.reason,
            referrer=register_child_response_dto.referrer,
            answers=tuple([RegisterChildResponseAnswerDtoMapper.to_domain_answer(answer) for answer in
                           register_child_response_dto.answers])
        )

        await self.__questionnaire_responses_repository.register_psychologist_child_questionnaire_response_async(
            psychologist.cedula,
            child.cedula,
            child.questionnaire_responses[-1]
        )
        return register_child_response_dto
