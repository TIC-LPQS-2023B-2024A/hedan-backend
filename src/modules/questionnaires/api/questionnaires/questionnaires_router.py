from fastapi import HTTPException

from fastapi import APIRouter
from fastapi_injector import Injected
from mediatr import Mediator

from src.modules.questionnaires.application.interactors.get_test_session_id.get_test_session_id_query import \
    GetTestSessionIdQuery
from src.modules.questionnaires.application.invitation_link.invitation_link_provider import InvitationLinkProvider

router = APIRouter(prefix="/questionnaires", tags=["Questionnaires"])


@router.get("/token/{child_id}/{psychologist_cedula}")
async def get_token(child_id: int, psychologist_cedula: int, mediator: Mediator = Injected(Mediator)):
    try:
        # Get test session id for the child
        query = GetTestSessionIdQuery(
            child_id=child_id,
            pyschologist_cedula=str(psychologist_cedula)
        )
        test_session_id = await mediator.send_async(query)
        # Validate if the test session id exists
        if test_session_id is None:
            raise HTTPException(status_code=404, detail="Test session not found")
        else:
            # Generate invitation link
            token = InvitationLinkProvider.generate_token(test_session_id)
            return f"http://127.0.0.1:8001/?token={token}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
