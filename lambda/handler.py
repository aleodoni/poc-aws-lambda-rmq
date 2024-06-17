from main.main import Main
from infra.conn.iconnect import IConnect
from infra.conn.alchemy.connect import SqlAlchemyConnect
from services.idata_service import IDataService
from services.data_service import DataService
from services.iqueue_service import IQueueService
from services.queue_service import QueueService

from infra.conn.fake.fake_connect import FakeConnect
from services.fake.fake_queue_service import FakeQueueService
from services.fake.fake_data_service import FakeDataService

def handler(event, context):
    conn: IConnect
    data_service: IDataService
    queue_service: IQueueService

    conn = SqlAlchemyConnect()
    data_service = DataService()
    queue_service = FakeQueueService()

    mainFlow = Main(conn, data_service, queue_service)

    print("Função lamda executada")
    mainFlow.connect()
    mainFlow.readMeetings()
    mainFlow.disconnect()
    mainFlow.send_meetings_to_queue()


if __name__ == "__main__":
    conn: IConnect
    data_service: IDataService
    queue_service: IQueueService
    
    # conn = SqlAlchemyConnect()
    # data_service = DataService()

    conn = FakeConnect()
    data_service = FakeDataService()
    # queue_service = FakeQueueService()
    queue_service = QueueService()

    mainFlow = Main(conn, data_service, queue_service)

    print("Função lambda executada localmente")
    mainFlow.connect()
    mainFlow.readMeetings()
    mainFlow.disconnect()
    mainFlow.send_meetings_to_queue()
    
    
