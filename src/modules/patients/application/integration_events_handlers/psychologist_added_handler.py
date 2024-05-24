from src.common.application.integration_event_handler import IntegrationEventHandler, TIntegrationEvent, TResponse
from src.modules.users_management.integration_events.psychologist_added_event import PsychologistAddedEvent


class PsychologistAddedEventHandler(IntegrationEventHandler[PsychologistAddedEvent, None]):
    async def handle(self, event: TIntegrationEvent) -> TResponse:
        # TODO: Save a psychologist in the database
        raise NotImplementedError()
