from typing import cast

from fastapi import FastAPI
from injector import Injector
from mediatr import Mediator

from src.common.api.router_installer import RouterInstaller
from src.common.application.event_bus import EventBus
from src.common.event_bus_setup import register_event_bus_handlers
from src.common.infrastructure.bus.memory.in_memory_event_bus import InMemoryEventBus
from src.common.mediator_setup import register_mediator_handlers
from src.common.module import Module
from src.modules.questionnaires.api.routers import routers
from src.modules.questionnaires.application.integration_events_handlers.integration_events_handlers import \
    event_handlers
from src.modules.questionnaires.application.interactors.handlers import handlers


class QuestionnairesModule(Module, RouterInstaller):
    @staticmethod
    def install(injector: Injector) -> None:
        # TODO: Install first the dependency injection services
        register_mediator_handlers(injector.get(Mediator), handlers)
        register_event_bus_handlers(cast(InMemoryEventBus, injector.get(EventBus)), event_handlers)

    @staticmethod
    def install_routers(fast_api_app: FastAPI):
        [fast_api_app.include_router(router) for router in routers]
