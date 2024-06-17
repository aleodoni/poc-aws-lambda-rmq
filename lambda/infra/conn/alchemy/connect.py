from sqlalchemy import create_engine, Engine

from infra.conn.iconnect import IConnect

class SqlAlchemyConnect(IConnect):
    def getEngine(self):
        engine=create_engine("postgresql://postgres:123456@localhost/spl",echo=True)

        return engine