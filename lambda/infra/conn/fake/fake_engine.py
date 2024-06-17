from typing import Self

class FakeEngine():
    def connect(self) -> Self:
        print("Opening fake connection")
        engine = self
        return self

    def close(self):
        print("Closing fake connection")