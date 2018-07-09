import BaseTypes.master
import _thread
import time
import communicator
import copy

class Master(BaseTypes.master.Master):
    waitingForAnswer : []

    def __init__(self, ports:[int] = [], workers:str = [], program = -1, state = 1, id: str = 'master'): # if program is -1 the program dosent distribute it
        self.coms = []
        port = ports
        print('master %s have been created' % id)
        print("")
        if len(port) != len(workers):
            raise ValueError("the number of the ports does not equal the number of the workers")
        for p in port:
            self.coms.append(communicator.Communicator(int(p), 'm'))
        self.id = id
        self.waitingForAnswer = []
        for w in workers:
            self.workersIds.append(w)
        for i in range(0, len(workers)):
            self.workersPort[self.workersIds[i]] = port[i]
            self.workersState[self.workersIds[i]] = 1
            self.waitingForAnswer.append(self.workersIds[i])
        self.program = program
        self.setMissions()
        self.answer = 0
        self.state = state

        #self.run()


    def setMissions(self):
        for w in range(0, len(self.workersIds)):
            self.workersMission.append(self.program)

    def run(self, state: int = -1):

        """man function of the master"""
        if state == -1:
            state = self.state
        if state == 1:
            self.setWorkers()
            print("setted workers")
            self.state = 3
            #time.sleep('3')
        if state == 3:
            print("waiting for an answer")
            if self.waitingToAnswer():
                print("answer is "+str(self.answer))
                return self.answer
        return self.run(self.state)

    def waitingToAnswer(self):
        """function wait for an answer from workers"""
        removeList = []
        for i in self.waitingForAnswer:
            origin, _, _, data, _ = self.coms[int(self.workersIds.index(i))].receive(str(self.id))
            if data is not None and int(data) > -1:
                ans = int(self.answer)
                ans += int(data)
                self.answer = ans
                removeList.append(i)

        for i in removeList:
            self.waitingForAnswer.remove(i)

        if len(self.waitingForAnswer) == 0:
            return True

        return False