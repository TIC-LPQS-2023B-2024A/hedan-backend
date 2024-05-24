from typing import cast

from fastapi import FastAPI
from injector import Injector

from src.common.api.router_installer import RouterInstaller
from src.common.application.event_bus import EventBus
from src.common.event_bus_setup import register_event_bus_handlers
from src.common.infrastructure.bus.memory.in_memory_event_bus import InMemoryEventBus
from src.common.module import Module
from src.modules.results_analysis.api.routers import routers
from src.modules.results_analysis.application.integration_events_handlers.integration_events_handlers import \
    game_event_handlers


class GameResultsAnalysisModule(Module, RouterInstaller):
    @staticmethod
    def install(injector: Injector) -> None:
        # TODO: Install first the dependency injection services
        register_event_bus_handlers(cast(InMemoryEventBus, injector.get(EventBus)), game_event_handlers)

    @staticmethod
    def install_routers(fast_api_app: FastAPI):
        [fast_api_app.include_router(router) for router in routers]
