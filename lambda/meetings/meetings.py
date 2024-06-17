from meetings.imeetings import IMeetings
from services.data_service import DataService

class Meetings(IMeetings):
    def read_meetings(self, connection):
        meetings_service = DataService()
        return meetings_service.get_meetings(connection)
