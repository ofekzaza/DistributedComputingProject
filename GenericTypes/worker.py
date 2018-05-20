from GenericTypes.genericWorker import BaseWorker
from communicator import Communicator

class Worker(BaseWorker):
    masterName: str
    answer: int

    def __init__(self, typ: str, name: str, masterName: str, port: int = 9999):
        if port > 9999 or port < 0:
            self.port = 9999
            raise ValueError("Illegal port value, Port value is now 9999")
        self.com = Communicator(port)
        self.port = port
        self.typ = typ
        self.name = name
        self.masterName = masterName
        self.answer = -1
        print("worker have been constructed")

    def main(self):
        data = -1
        while data is -1:
            data = self.com.recive(self.name)
