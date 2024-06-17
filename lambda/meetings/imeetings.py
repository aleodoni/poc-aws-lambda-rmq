from abc import ABC, abstractmethod

class IMeetings(ABC):
    @abstractmethod
    def read_meetings(self, connection):
        pass