import communicator

class Master:
    coms: [communicator.Communicator] = []
    ports = []
    name: str = 'master'
    workers = [] #the name of the master could be just id, defult -1
    id: int
    typ: str = "worker"
    state: int = 1 #state machine: 1 - getting information, 2 - proccesing and sending results
    returnTarget: str = -1 #defult
    mission:str
    curTarger:str
    workersMission = []
    program:str
    workersState = []

    def __init__(self, name: str = 'master', id: int = -1, ports:[int] = [], workers:str = [], program = -1): # if program is -1 the program dosent distribute it
        print('master have been created')
        if len(ports) != len(workers):
            assert "the number of the ports does not equal the number of the workers"
        for p in ports:
            self.coms.append(communicator.Communicator(p))
        self.ports = ports
        self.id = id
        self.workers = workers
        self.name = name
        self.program = program

    def run(self, state: int = -1):
        "man function of the master"
        if state == -1:
            state = self.state

        if state == 1:
            self.setMaster()
        if state == 2:
            self.setWorkers()
        return True

    def setMaster(self, option: int = 1): #option 1 is wait, 2 is dont wait, you can add more
        "gives the master the base program from an outside code"
        if option == 1:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.waitRecive(self.name)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))
        elif option == 2:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.recive(self.name)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))

    def setWorkers(self):
        "set all the workers in the list"
        for i in range(0, len(self.workers)):
            self.coms[i].send(self.name, self.workers[i], -1, self.workersMission[i])

    def setProgram(self):#dosent works it
        "dosent work yet"
        if self.program == -1:
            pass
        pass

    def addWorker(self, id:int, port:int):
        "add a new worker to this current master"
        self.workers.append(id)
        self.ports.append(port)
        self.coms.append(communicator.Communicator(port))
        print("new worker number: %s have been created" %(str(id)))

    def printWorkers(self):
        print("Workers of master number "+str(self.id)+" are:")
        for i in range(0, len(self.workers)):
            print("worker number: %s have port number: %s and he is in state number: %s" % (str(self.workers[i]), str(self.ports[i])))


    def run(self):
        pass

    def __del__(self):
        print('master have died number %s died' % (str(self.id)))

