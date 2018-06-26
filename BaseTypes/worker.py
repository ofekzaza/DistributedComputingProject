import communicator

class Worker:
    com: communicator.Communicator
    port:int
    name: str
    master = None #the name of the master could be just id, defult -1
    id: int
    typ: str = "worker"
    state: int = 1 #state machine: 1 - getting information, 2 - proccesing and sending results
    returnTarget: str = -1 #defult
    mission:str
    curReciver: str # the current worker which the worker got data from, or expected

    def __init__(self, name: str, id: int, port:int = 9999, master:str = -1):
        self.com = communicator.Communicator(port)
        self.port = port
        self.id = id
        self.master = master
        self.name = name
        self.curReciver = master

    def run(self, state:int = -1):
        if state == -1:
            state = self.state
        if state == 1:
            self.setWorker()
        if state == 2:
            self.run()
        return True

    def setWorker(self, option: int = 1): #option 1 is wait, 2 is dont wait, you can add more
        if option == 1:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.waitRecive(self.name)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))
        elif option == 2:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.recive(self.name)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))

    def run(self):
        pass

    def __del__(self):
        self.com.__del__()
        print('worker number %s died' % (str(self.id)))

