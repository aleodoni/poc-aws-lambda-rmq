from infra.conn.iconnect import IConnect
from infra.conn.fake.fake_engine import FakeEngine

class FakeConnect(IConnect):
    def getEngine(self) -> FakeEngine:
        engine = FakeEngine()
        return engine
