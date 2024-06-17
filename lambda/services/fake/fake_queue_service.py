from services.iqueue_service import IQueueService

class FakeQueueService(IQueueService):
    def send_meetings(self, meetings: str):
        print("Enviando reuniões para a fila FAKE...")
        print(meetings)
        print("Reuniões enviadas !")
    