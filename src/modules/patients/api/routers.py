from typing import List

from fastapi import APIRouter

from src.modules.patients.api.psychologist.ejemplo_psychologist_router import router as psychologist_router

routers: List[APIRouter] = [
    psychologist_router
]
