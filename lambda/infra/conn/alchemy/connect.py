from sqlalchemy import create_engine
import os

from infra.conn.iconnect import IConnect

class SqlAlchemyConnect(IConnect):
    def getEngine(self):
        host = os.environ["HOST"]

        engine=create_engine("postgresql://postgres:123456@" + host + "/spl",echo=True)

        return engine