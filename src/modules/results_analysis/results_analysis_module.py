from typing import cast

from injector import Injector

from src.common.application.event_bus import EventBus
from src.common.event_bus_setup import register_event_bus_handlers
from src.common.infrastructure.bus.memory.in_memory_event_bus import InMemoryEventBus
from src.common.module import Module
from src.modules.results_analysis.application.integration_events_handlers.integration_events_handlers import \
    game_event_handlers


class ResultsAnalysisModule(Module):
    @staticmethod
    def install(injector: Injector) -> None:
        register_event_bus_handlers(cast(InMemoryEventBus, injector.get(EventBus)), game_event_handlers)
