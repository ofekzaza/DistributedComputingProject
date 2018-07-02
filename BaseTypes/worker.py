import communicator

class Worker:
    com: communicator.Communicator
    port:int
    master: int #the name of the master could be just id, defult -1
    id: int
    """dont change id after setup, if you want go to master, kill worker and create a new one"""
    typ: str = "worker"
    state: int = 1 #state machine: 1 - getting information, 2 - proccesing and sending results
    returnTarget: str = -1 #defult
    mission:str
    curReciver: str # the current worker which the worker got data from, or expected
    answer: str
    emg:communicator.Emergency

    def __init__(self,id: int, port:int = 9999, master:str = 'master'):
        self.com = communicator.Communicator(port, id, "worker")
        self.port = port
        self.id = id
        self.master = master
        self.curReciver = master
        self.run()

    def setState(self, state:int): # state -999 is dosent work and -1 is defult at start
        if state < -999:
            print("Illegal State input to worker "+ self.id)
        else:
            self.state = state
            print("Worker %s state have been updated to state %s" % (self.id, self.state))


    def run(self):
        self.check()

        if self.state == -999:
            return False
        if self.state == -1:
            state = self.state
        if self.state == 1:
            self.startWorker()
        if self.state == 2:
            self.run()
        return True

    def startWorker(self, option: int = 1): #option 1 is wait, 2 is dont wait, you can add more
        if option == 1:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.waitRecive(self.id)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))
        elif option == 2:
            self.curReciver, errorCheck, self.returnTarget, self.mission = self.com.recive(self.id)
            if errorCheck != self.name:
                print('Worker number %s got the wrong input' % (str(self.id)))

    def returnAnswer(self, target = 'master'):
        """Send answer to target, defult target is master"""
        return self.com.send(self.id, target, -1, self.answer)

    def printWorker(self):
        print("Worker number %s, port number %s, in state %s, master is %s" % (str(self.id),str(self.port),str(self.state), str(self.master)))

    def check(self):
        if self.emg.listen():
            self.__del__()

        if self.master is None or self.com is None or self.id >= 0:
            print("Worker number %s is not functional" % str(self.id))


    def __del__(self):
        #pass
        self.com.__del__()
        print('worker number %s died' % (str(self.id)))

        if False:
            """pls don't"""
            self.__del__()