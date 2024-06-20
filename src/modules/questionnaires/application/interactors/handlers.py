from typing import Type, Union

from src.common.application.command_handler import CommandHandler
from src.common.application.query_handler import QueryHandler
from src.modules.questionnaires.application.interactors.add_test_session.add_test_session_command_handler import \
    AddTestSessionCommandHandler
from src.modules.questionnaires.application.interactors.get_test_session_id.get_test_session_id_query_handler import \
    GetTestSessionIdQueryHandler
from src.modules.questionnaires.application.interactors.set_test_answers.set_test_answers_command_handler import \
    SetTestAnswersCommandHandler
from src.modules.questionnaires.application.interactors.validate_questionnaire_token.validate_questionnaire_token_query_handler import \
    ValidateQuestionnaireTokenQueryHandler

handlers: list[Type[Union[CommandHandler, QueryHandler]]] = [
    AddTestSessionCommandHandler,
    GetTestSessionIdQueryHandler
]

game_handlers: list[Type[Union[CommandHandler, QueryHandler]]] = [
    ValidateQuestionnaireTokenQueryHandler,
    SetTestAnswersCommandHandler
]
