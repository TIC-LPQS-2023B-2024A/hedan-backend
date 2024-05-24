from typing import Type, Union

from src.common.application.command_handler import CommandHandler
from src.common.application.query_handler import QueryHandler

handlers: list[Type[Union[CommandHandler, QueryHandler]]] = [

]

game_handlers: list[Type[Union[CommandHandler, QueryHandler]]] = [

]
