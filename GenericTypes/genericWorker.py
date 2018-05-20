import communicator


class BaseWorker:
    """This class is the base class of each worker and master in the project"""
    com: communicator.Commuicator #Communication
    port: int #"""communication port"""
    typ: str #type
    name: str
    mission: str

    def __init__(self, typ: str, name: str, port: int = 9999):
        if port > 9999 or port < 0:
            self.port = 9999
            raise ValueError("Illegal port value, Port value is now 9999")
        self.com = communicator.Communicator(port)
        self.port = port
        self.typ = typ
        self.name = name

    def main(self):
        pass

    def __del__(self):
        self.com.__del__()