from typing import Type, Union

from src.common.application.command_handler import CommandHandler
from src.common.application.query_handler import QueryHandler
from src.modules.users_management.application.interactors.add_psychologist_user.add_psychologist_user_command_handler import \
    AddPsychologistUserCommandHandler
from src.modules.users_management.application.interactors.login.login_command_handler import LoginCommandHandler

handlers: list[Type[Union[CommandHandler, QueryHandler]]] = [
    AddPsychologistUserCommandHandler,
    LoginCommandHandler
]
