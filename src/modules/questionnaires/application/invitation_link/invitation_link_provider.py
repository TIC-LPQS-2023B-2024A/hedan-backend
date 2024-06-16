# application/invitation_link/invitation_link_provider.py
import os

import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv("SECRET_KEY")


class InvitationLinkProvider:
    @staticmethod
    def generate_token(test_session_id: int) -> str:
        payload = {
            "test_session_id": test_session_id,
            "exp": datetime.now(tz=timezone.utc) + timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def decode_token(token: str):
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
