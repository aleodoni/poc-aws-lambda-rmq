from typing import Any
import pika
import pika.channel

from services.iqueue_service import IQueueService

class QueueService(IQueueService):
    queue_name = 'spl_meetings_queue'
    credentials: pika.PlainCredentials
    connection: pika.BlockingConnection
    channel: Any

    def __init__(self):
        self.credentials = pika.PlainCredentials('rabbit', '123456')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, '/', self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        
    def send_meetings(self, meetings: str):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=meetings
        )
    