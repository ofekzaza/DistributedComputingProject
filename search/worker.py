import BaseTypes.worker

class Worker (BaseTypes.worker.Worker):


    def run(self, state = -1):
        print('a')
        if state == -1:
            state = self.state
        self.state = state

        print("worker number "+ str(self.id)+"is working?!?!??!?!?")

        if self.state == -999:
            return False

        if self.state == -1:
            state = self.state
            self.printWorker()

        if self.state == 1:
            self.startWorker()
            self.state = 2

        if self.state == 2:
            self.answer = self.search()
            self.com.send(self.id, self.master, -1, self.answer)
            #self.check()
            print(("message is %s,%s,%s,%s")%(self.id, self.master, -1, self.search()))
            return self.answer
        return self.run()

    def search(self, file = -999):
        """serach target in file"""

        print("search")

        if file == -999:
            file = str(str(self.id)+".txt")
        file = open(str(file), 'r')
        target = str(self.mission)

        counter = 0 # the number of times which target appeared in file

        l = len(target)

        read = file.read(l)

        n = read[l-1]
        while n is not '':
            if str(read)  == str(target):
                counter += 1
            n = file.read(l)
            read = str(read[:0] + n)
        print("worker number %s have answer which is %s" % (self.id, counter))
        return str(counter)


