from services.idata_service import IDataService
from infra.conn.iconnect import IConnect

class GetMeetingsUseCase:
    data_service: IDataService
    connection: IConnect

    def __init__(self, connection, data_service: IDataService):
        self.connection = connection
        self.data_service = data_service

    def execute(self):
        meetings = self.data_service.get_meetings(self.connection)
        return meetings