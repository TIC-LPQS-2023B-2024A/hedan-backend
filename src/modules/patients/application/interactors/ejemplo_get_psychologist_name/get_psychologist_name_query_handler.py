from injector import Inject

from src.common.application.query_handler import QueryHandler
from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.get_psychologist_name_query import \
    GetPsychologistNameQuery
from src.modules.patients.application.interactors.ejemplo_get_psychologist_name.psychologist_name_query_service import \
    PsychologistNameQueryService


class GetPsychologistNameQueryHandler(QueryHandler[GetPsychologistNameQuery, str]):
    def __init__(
            self,
            psychologist_name_query_service: Inject[PsychologistNameQueryService]
    ):
        self.__psychologist_name_query_service = psychologist_name_query_service

    async def handle(self, query: GetPsychologistNameQuery) -> str:
        return await self.__psychologist_name_query_service.execute_async(query)
