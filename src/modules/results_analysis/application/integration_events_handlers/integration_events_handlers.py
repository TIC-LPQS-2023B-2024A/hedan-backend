from typing import List, Dict, Type

from src.common.application.integration_event_handler import IntegrationEventHandler
from src.common.integration_events.integration_event import IntegrationEvent
from src.modules.questionnaires.integration_events.test_answers_submitted_event import TestAnswersSubmittedEvent
from src.modules.results_analysis.application.integration_events_handlers.test_answers_submitted_event_handler import \
    TestAnswersSubmittedEventHandler

game_event_handlers: List[Dict[Type[IntegrationEvent], Type[IntegrationEventHandler]]] = [
    {
        TestAnswersSubmittedEvent: TestAnswersSubmittedEventHandler
    }
]

