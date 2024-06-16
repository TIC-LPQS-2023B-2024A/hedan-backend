from typing import List

from fastapi import APIRouter

from src.modules.questionnaires.api.questionnaires.questionnaires_router import router as questionnaires_router

routers: List[APIRouter] = [
    questionnaires_router
]

game_routers: List[APIRouter] = [

]