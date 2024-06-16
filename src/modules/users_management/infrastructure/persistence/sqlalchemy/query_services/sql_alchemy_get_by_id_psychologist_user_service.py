from abc import ABC

from injector import Inject
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select as future_select
from sqlalchemy.exc import NoResultFound

from src.common.domain.value_objects.cedula import Cedula
from src.common.domain.value_objects.sex import Sex
from src.modules.users_management.application.interactors.get_psychologist_user.get_by_id_psychologist_query import \
    GetByIdPsychologistQuery
from src.modules.users_management.application.interactors.get_psychologist_user.get_by_id_psychologist_response import \
    GetByIdPsychologistResponse
from src.modules.users_management.application.interactors.get_psychologist_user.get_by_id_psychologist_service import \
    GetByIdPsychologistService
from src.modules.users_management.infrastructure.persistence.sqlalchemy.models.user_model import UserModel
from src.modules.patients.infrastructure.persistence.sqlalchemy.models.psychologist_model import PsychologistModel


class SQLAlchemyGetByIdPsychologistUserService(GetByIdPsychologistService):
    def __init__(self, async_session_factory: Inject[async_sessionmaker[AsyncSession]]):
        self.__async_session_factory = async_session_factory

    async def execute_async(self, query: GetByIdPsychologistQuery) -> GetByIdPsychologistResponse:
        try:
            async with self.__async_session_factory() as session:
                # Query to find the user associated with the psychologist
                user_query = select(UserModel).where(UserModel.psychologist_cedula == query.cedula)
                user_result = await (session.execute(user_query))
                user = user_result.scalar_one()

                # Query to find the psychologist
                psychologist_query = future_select(PsychologistModel).where(PsychologistModel.cedula == query.cedula)
                psychologist_result = await (session.execute(psychologist_query))
                psychologist = psychologist_result.scalar_one()

                # Build the response object
                return GetByIdPsychologistResponse(
                    cedula=psychologist.cedula,
                    name=psychologist.name,
                    sex=Sex(psychologist.sex),
                    email=user.email
                )

        except NoResultFound:
            # Handle case where either psychologist or user is not found
            return None

        except Exception as e:
            # Handle other exceptions
            raise e
