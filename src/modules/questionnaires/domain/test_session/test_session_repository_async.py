from abc import ABC, abstractmethod

from src.modules.questionnaires.domain.test_session.answers_set import AnswerSet
from src.modules.questionnaires.domain.test_session.test_session import TestSession


class TestSessionRepositoryAsync(ABC):
    ...

    async def add_test_session(self, test_session):
        pass

    @abstractmethod
    async def set_answers_set(self, test_session_id: int, answer_set: AnswerSet) -> TestSession:
        pass
