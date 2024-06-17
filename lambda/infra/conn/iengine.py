from abc import ABC, abstractmethod
from typing import Self

class IEngine(ABC):
    @abstractmethod
    def connect(self) -> Self:
        pass

    def close(self):
        pass