from fastapi import FastAPI
from fastapi_injector import attach_injector, InjectorMiddleware
from injector import Injector

from src.di import add_dependencies
from src.game_api import game_api
from src.web_page_api import web_page_api


def create_fast_api_app() -> FastAPI:
    app = FastAPI()

    app.include_router(game_api.router)
    app.include_router(web_page_api.router)

    injector = Injector()
    injector = add_dependencies(injector)

    app.add_middleware(InjectorMiddleware, injector=injector)

    attach_injector(app, injector)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    return app
