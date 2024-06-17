from services.iqueue_service import IQueueService

class SendMeetingsUseCase:
    queue_service : IQueueService

    def __init__(self, queue_service: IQueueService):
        self.queue_service = queue_service

    def execute(self, meetings: str):
        self.queue_service.send_meetings(meetings)