import _thread
import search.worker
import search.master

class Init():
    def init(searchTarget:str):
        ids = []
        workers: [search.worker.Worker] = []
        ports = []
        com = []

        for i in range(0, 10):
            workers.append(search.worker.Worker(i, 9999 - i))
            ids.append(i)
            ports.append(9999 - i)

        master = search.master.Master(ports, ids, 'a')

        _thread.start_new_thread(master.run, ())
        print("thread have been created")

        print("lenght of worker list:" + str(len(workers)))
        _thread.start_new_thread(workers[0].run(), ())
        _thread.start_new_thread(workers[1].run(), ())
        _thread.start_new_thread(workers[2].run(), ())
        _thread.start_new_thread(workers[3].run(), ())
        _thread.start_new_thread(workers[4].run(), ())
        _thread.start_new_thread(workers[5].run(), ())
        _thread.start_new_thread(workers[6].run(), ())
        _thread.start_new_thread(workers[7].run(), ())
        _thread.start_new_thread(workers[8].run(), ())
        _thread.start_new_thread(workers[9].run(), ())
"""
        _thread.start_new_thread(search.worker.Worker(, 9999 - i), ())
        _thread.start_new_thread(workers[1].run(), ())
        _thread.start_new_thread(workers[2].run(), ())
        _thread.start_new_thread(workers[3].run(), ())
        _thread.start_new_thread(workers[4].run(), ())
        _thread.start_new_thread(workers[5].run(), ())
        _thread.start_new_thread(workers[6].run(), ())
        _thread.start_new_thread(workers[7].run(), ())
        _thread.start_new_thread(workers[8].run(), ())
        _thread.start_new_thread(workers[9].run(), ())
"""
Init.init('a')