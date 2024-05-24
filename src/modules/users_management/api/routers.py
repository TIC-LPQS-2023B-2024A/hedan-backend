from typing import List

from fastapi import APIRouter

from src.modules.users_management.api.auth_router import router as auth_router

routers: List[APIRouter] = [
    auth_router,
]
