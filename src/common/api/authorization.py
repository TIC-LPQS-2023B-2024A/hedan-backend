from functools import wraps

from fastapi import Security, HTTPException
from fastapi_jwt import JwtAuthorizationCredentials

from src.common.application.user_role import UserRole
from src.common.infrastructure.token.access_security import access_security


def admin_only(credentials: JwtAuthorizationCredentials = Security(access_security)):
    if credentials["role"] != UserRole.ADMIN:
        raise HTTPException(status_code=403)


def psychologist_only(credentials: JwtAuthorizationCredentials = Security(access_security)):
    if credentials["role"] != UserRole.PSYCHOLOGIST:
        raise HTTPException(status_code=403)
