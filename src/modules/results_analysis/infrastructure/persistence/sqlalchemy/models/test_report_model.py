from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.common.infrastructure.persistence.sqlalchemy.base import Base
from src.modules.results_analysis.domain.test_report.test_results import TestResults


class TestReportModel(Base):
    __tablename__ = "test_reports"
    __table_args__ = {"schema": "results_analysis"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    psychologist_cedula: Mapped[str]
    test_session_id: Mapped[int]
    child_age: Mapped[int]
    scholar_grade: Mapped[int]
    date_time_of_answer: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=None, nullable=True,
                                                          server_default=func.now())
    test_results: Mapped[TestResults] = mapped_column(JSONB, default=None, nullable=True)