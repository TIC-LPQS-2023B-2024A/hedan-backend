from fastapi import FastAPI
from injector import Injector
from mediatr import Mediator

from src.common.api.router_installer import RouterInstaller
from src.common.mediator_setup import register_mediator_handlers
from src.common.module import Module
from src.modules.results_analysis.api.routers import routers
from src.modules.results_analysis.application.interactors.handlers import handlers


class ResultsAnalysisModule(Module, RouterInstaller):
    @staticmethod
    def install(injector: Injector) -> None:
        # TODO: Install first the dependency injection services
        register_mediator_handlers(injector.get(Mediator), handlers)

    @staticmethod
    def install_routers(fast_api_app: FastAPI):
        [fast_api_app.include_router(router) for router in routers]
