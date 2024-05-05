from abc import ABC, abstractmethod


class TokenHelper(ABC):
    @abstractmethod
    def generate_token(self, payload: dict) -> str:
        pass

    @abstractmethod
    def validate_token(self, token: str) -> bool:
        pass

    @abstractmethod
    def get_payload(self, token: str) -> dict:
        pass
