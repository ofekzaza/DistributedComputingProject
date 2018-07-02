import BaseTypes.worker

class Worker (BaseTypes.worker.Worker):


    def run(self):
        self.check()
        if self.state == -999:
            return False

        if self.state == -1:
            state = self.state
            self.printWorker()

        if self.state == 1:
            self.startWorker()

        if self.state == 2:
            self.send(self.id, self.master, -1, self.search())

        return True

    def search(self):
        """serach target in file"""
        helper = self.mission.split("...")
        file = open(str(helper[0]), 'r')
        target = str(helper[1])

        counter = 0 # the number of times which target appeared in file

        l = len(target)

        read = file.read(l)
        n = read[1]
        while n is not '':
            if read  == target:
                counter += 1
            n = file.read(1)
            read = str(read[:1] + n)
        return counter

