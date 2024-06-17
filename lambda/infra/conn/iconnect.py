from abc import ABC, abstractmethod

from infra.conn.iengine import IEngine

class IConnect(ABC):
    @abstractmethod
    def getEngine(self) -> IEngine:
        pass
