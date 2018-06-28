import communicator

class Master:
    coms: [communicator.Communicator] = []
    workersIds = []
    workersPort = {}
    workersMission = {}
    id: int = 'master'
    typ: str = "worker"
    state: int = 1 #state machine: 1 - getting information, 2 - proccesing and sending results
    returnTarget: str = -1 #defult
    mission:str
    curTarger:str
    program:str
    emg: communicator.Emergency

    def __init__(self, id: str = 'master', ports:[int] = [], workers:str = [], program = -1): # if program is -1 the program dosent distribute it
        port = ports
        print('master %s have been created' % id)

        print("port " + str(port[1]))
        if len(port) != len(workers):
            assert "the number of the ports does not equal the number of the workers"
        for p in port:
            self.coms.append(communicator.Communicator(int(p), 'm'))
        self.id = id
        for w in workers:
            self.workersIds.append(w)
        for i in range(0, len(workers)):
            self.workersPort[workers[i]] = port[i]
        self.program = program
        self.emg = communicator.Emergency(True)
        print()

    def run(self, state: int = -1):
        """man function of the master"""
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
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.waitRecive(self.id)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))
        elif option == 2:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.recive(self.id)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))

    def setWorkers(self):
        """set all the workers in the list"""
        for i in range(0, len(self.workers)):
            self.coms[i].send(self.name, self.workersIds[i], -1, self.workersMission[i])

    def setProgram(self):#dosent works it
        """dosent work yet"""
        if self.program == -1:
            pass
        pass

    def addWorker(self, id:int, port:int):
        """add a new worker to this current master"""
        idd = id
        if idd == -1 or idd in self.workersIds:
            for i in range(len(self.workersIds)):
                if i != self.workersIds[i]:
                    idd = i
            if idd == -1 or id in self.workersIds:
                idd = len(self.workersIds)+1
            print("the id is not the original givven id, the new id is " +idd)
        self.workersIds.append(idd)
        self.workersPort[idd] = port
        self.coms.append(communicator.Communicator(port))
        print("new worker number: %s have been created" %(str(idd)))

    def printWorkers(self):
        print(self.workersIds[0])
        print("Workers of master number "+str(self.id)+" are:")
        for i in self.workersIds:
            print("worker number: %s have port number: %s and he is in state number: %s" % (str(i), str(self.workersPort.get(i))))

    def listenAll(self):
        """function auto search any input from workers"""
        returnValue = [[],[],[],[]]
        i = 0
        for c in self.coms:
            returnValue[0][i], returnValue[1][i], returnValue[2][i], returnValue[3][i] = c.recive(self.id)
            i += 1
        return  returnValue[0], returnValue[1], returnValue[2], returnValue[3]

    def listen(self, port):
        return self.coms[self.ports.index(port)]

    def run(self):
        pass

    def killWorker(self, id):
        if id in self.workersIds:
            self.emg.kill(id)
            print("worker number %s have been commanded to die" % str(id))
        else:
            print("Illegal input to killWorker")

    def __del__(self):
        for id in self.workersIds:
            self.killWorker(id)
        print('master have died number %s died' % (str(self.id)))

