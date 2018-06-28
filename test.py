import communicator
import BaseTypes.master
import BaseTypes.worker
import socket
import time
#work = BaseTypes.worker.Worker(1,1,1)

#work.printWorker()



c = communicator.Communicator(10000, 'c')
ids = []
workers: [BaseTypes.worker.Worker] = []
ports = []
com = []


for i in range(0, 10):
    workers.append(BaseTypes.worker.Worker(i, 9999-i))
    ids.append(i)
    ports.append(9999-i)

master = BaseTypes.master.Master('master', ids, ports)

master.printWorkers()