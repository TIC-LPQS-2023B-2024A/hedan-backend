from src.common.application.integration_event_handler import IntegrationEventHandler, TIntegrationEvent, TResponse
from src.modules.questionnaires.integration_events.test_answers_submitted_event import TestAnswersSubmittedEvent


class TestAnswersSubmittedEventHandler(IntegrationEventHandler[TestAnswersSubmittedEvent, None]):
    async def handle(self, event: TestAnswersSubmittedEvent) -> None:
        # TODO: Save a test_report of the child test_report
        raise NotImplementedError()
