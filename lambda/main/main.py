from .imain import IMain
from meetings.domain.use_cases.get_meetings.get_meetings_use_case import GetMeetingsUseCase
from meetings.domain.use_cases.send_meetings.send_meetings_use_case import SendMeetingsUseCase

class Main(IMain):
    meetings: str

    def __init__(self, conn, data_service, queue_service):
        super().__init__(conn, data_service, queue_service)

    def connect(self):
        print("Realizando conexão com BD")
        engine  = self.conn.getEngine()
        self.connection = engine.connect()
        

    def readMeetings(self): 
        print("Lendo reuniões do dia")
        get_meetings_use_case = GetMeetingsUseCase(self.connection, self.data_service)
        self.meetings = get_meetings_use_case.execute()

    def send_meetings_to_queue(self):
        send_meetings_use_case = SendMeetingsUseCase(self.queue_service)
        send_meetings_use_case.execute(self.meetings)

    def disconnect(self):
        print("Encerrando conexão com BD")
        self.connection.close()