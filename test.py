import communicator
import BaseTypes.master
import BaseTypes.worker
import socket
import time
import search.worker
import search.master
import _thread

import search.master

ports = []
ids = []

for x in range(1):
    ports.append(9999-x)
    ids.append(x)

w1 = search.worker.Worker(0,9999)

master = search.master.Master(ports, ids, 'a')


_thread.start_new_thread(master.run, ())

print("hello")

w1.run()


"""
_thread.start_new_thread(master.run(), ())

_thread.start_new_thread(w1.run(), ())"""