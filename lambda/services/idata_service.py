from abc import ABC, abstractmethod

class IDataService(ABC):
    @abstractmethod
    def get_meetings(self, connection):
        pass