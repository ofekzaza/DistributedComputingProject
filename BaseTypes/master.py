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
    workersState = {}
    listenTarget: int
    emg = communicator.Emergency(True)


    def __init__(self, id: str = 'master', ports:[int] = [], workers:str = [], program = -1): # if program is -1 the program dosent distribute it
        port = ports
        print('master %s have been created' % id)
        if len(port) != len(workers):
            assert "the number of the ports does not equal the number of the workers"
        for p in port:
            self.coms.append(communicator.Communicator(int(p), 'm'))
        self.id = id
        for w in workers:
            self.workersIds.append(w)
        for i in range(0, len(workers)):
            self.workersPort[self.workersIds[i]] = port[i]
            self.workersState[self.workersIds[i]] = 1
        self.program = program
        self.run()

    def run(self, state: int = -1):
        """man function of the master"""
        if state == -1:
            state = self.state
        if state == 1:
            self.setMaster()
        if state == 2:
            self.setWorkers()
        if state == 3:
            self.listen()
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
        self.state = 3

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
        print("Workers of master number "+str(self.id)+" are:")
        for i in self.workersIds:
            print("worker number '%s' have port number '%s'" % (str(i), str(self.workersPort[i])))
        print("")

    def listenAll(self):
        """function auto search any input from workers"""
        returnValue = [[],[],[],[]]
        i = 0
        for c in self.coms:
            returnValue[0][i], returnValue[1][i], returnValue[2][i], returnValue[3][i] = c.recive(self.id)
            i += 1
        return  returnValue[0], returnValue[1], returnValue[2], returnValue[3]

    def listenPort(self, port):
        return self.coms[self.ports.index(port)]

    def listen(self):
        return self.coms[self.workersIds.index(self.listenTarget)]

    def killWorker(self, id):
        if id in self.workersIds:
            self.coms[self.workersIds.index(id)].kill(id)
            print("worker number %s have been commanded to die" % str(id))
        else:
            print("Illegal input to killWorker")

    def setStage(self, stage):
        self.state = stage
        print("master stage have been changed")

    def __del__(self):
        for id in self.workersIds:
            self.killWorker(id)
        self.emg.__del__()
        print('master have died number %s died' % (str(self.id)))

