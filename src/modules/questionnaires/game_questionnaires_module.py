from typing import cast

from fastapi import FastAPI
from injector import Injector
from mediatr import Mediator

from src.common.api.router_installer import RouterInstaller
from src.common.mediator_setup import register_mediator_handlers
from src.common.module import Module
from src.modules.questionnaires.api.routers import game_routers
from src.modules.questionnaires.application.interactors.handlers import game_handlers


class GameQuestionnairesModule(Module, RouterInstaller):
    @staticmethod
    def install(injector: Injector) -> None:
        # TODO: Install first the dependency injection services
        register_mediator_handlers(injector.get(Mediator), game_handlers)

    @staticmethod
    def install_routers(fast_api_app: FastAPI):
        [fast_api_app.include_router(router) for router in game_routers]
