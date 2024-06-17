from abc import ABC, abstractmethod

from infra.conn.iconnect import IConnect
from services.idata_service import IDataService
from services.iqueue_service import IQueueService

class IMain(ABC):
    conn: IConnect
    data_service: IDataService
    queue_service: IQueueService

    def __init__(self, conn, data_service, queue_service):
        self.conn = conn
        self.data_service = data_service
        self.queue_service = queue_service

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def readMeetings(self) -> str:
        pass

    @abstractmethod
    def send_meetings_to_queue(self):
        pass
