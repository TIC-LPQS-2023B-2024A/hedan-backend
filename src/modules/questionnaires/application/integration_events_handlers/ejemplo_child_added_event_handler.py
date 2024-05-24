from src.common.application.integration_event_handler import IntegrationEventHandler
from src.modules.patients.integration_events.child_added_event import ChildAddedEvent


class ChildAddedEventHandler(IntegrationEventHandler[ChildAddedEvent, None]):
    async def handle(self, event: ChildAddedEvent) -> None:
        print("El módulo de pacientes agregó un niño")
        print(event)
