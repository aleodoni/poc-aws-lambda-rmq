from abc import ABC, abstractmethod

class IQueueService(ABC):
    @abstractmethod
    def send_meetings(self, meetings: str):
        pass