import communicator
import BaseTypes.master
import BaseTypes.worker
import socket

#work = BaseTypes.worker.Worker(1,1,1)

#work.printWorker()



c = communicator.Communicator(10000)
ids = []
workers: [BaseTypes.worker.Worker] = []
ports = []
com = []

d = communicator.Communicator(10000)

c.send('a','a','a','a')

print(d.receive('a'))

for i in range(0, 10):
    #com.append(d)
    #workers.append(BaseTypes.worker.Worker(i, 9999-i))
    #ids.append(i)
    #ports.append(5050)
    pass

#workers.append(BaseTypes.worker.Worker(1,9999,1))

#master = BaseTypes.master.Master('master', [1], [1])

#master.printWorkers()

d.__del__()
c.__del__()
