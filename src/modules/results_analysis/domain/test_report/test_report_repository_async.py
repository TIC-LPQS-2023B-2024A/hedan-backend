from abc import ABC, abstractmethod

from src.modules.results_analysis.domain.test_report.test_report import TestReport


class TestReportRepositoryAsync(ABC):
    @abstractmethod
    async def add_test_report(self, test_report: TestReport):
        ...
