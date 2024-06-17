from sqlalchemy import text
import pandas as pd
import json

from services.idata_service import IDataService

class DataService(IDataService):
    def get_meetings(self, connection):
        sql = text('SELECT * FROM reunioes')

        dataFrame = pd.read_sql(sql,connection)
        result_json = dataFrame.to_json(orient="records", default_handler=str)
        result_str = json.dumps(result_json)

        return result_str
