from dataclasses import dataclass


@dataclass(frozen=True)
class Cedula:
    value: str

    def __post_init__(self):
        pass

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value
