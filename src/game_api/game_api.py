from fastapi import APIRouter

from src.game_api.routers.questionnaire_response import questionnaire_response_router

router = APIRouter(prefix="/game", tags=["game"])
router.include_router(questionnaire_response_router)
