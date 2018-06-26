import communicator
import BaseTypes.master
import BaseTypes.worker

master = BaseTypes.master.Master('master', -1, [], [])

master.addWorker(0, 9999)

master.printWorkers()