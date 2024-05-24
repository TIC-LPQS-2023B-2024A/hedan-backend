from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.common.infrastructure.persistence.sqlalchemy.base import Base
from src.modules.questionnaires.domain.test_session.answer import Answer
from src.modules.questionnaires.domain.test_session.test_results import TestResults


class TestSessionModel(Base):
    __tablename__ = "test_sessions"
    __table_args__ = {"schema": "questionnaires"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    psychologist_cedula: Mapped[str]
    child_age: Mapped[int]
    scholar_grade: Mapped[int]
    date_time_of_answer: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=None, nullable=True,
                                                          server_default=func.now())
    answers: Mapped[list[Answer]] = mapped_column(JSONB, default=None, nullable=True)
    test_results: Mapped[TestResults] = mapped_column(JSONB, default=None, nullable=True)
