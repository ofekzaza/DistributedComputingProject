from GenericTypes.genericWorker import BaseWorker
from communicator import Communicator

class Master(BaseWorker):
    answer: int
    clientNames: [str]
    type = "Master"

    def __init__(self, typ: str, name: str, clientsName: [str], port: int = 9999):
        if port > 9999 or port < 0:
            self.port = 9999
            raise ValueError("Illegal port value, Port value is now 9999")
        self.com = Communicator(port)
        self.port = port
        self.typ = typ
        self.name = name
        self.clientNames = clientsName
        self.answer = -1
        print("master have been constructed")

    def main(self):
        for client in self.clientNames:
            pass




