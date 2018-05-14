from abc import ABCMeta
import socket
import time

class Comunicator(metaclass=ABCMeta):


    def send(self, origin:str, target:str, returnTarget:str, msg:str):
        "the function is sending data "
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating the socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # added in order to fix the bug the may accure
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # socket is broadcasting

        message: str = "Origin:{0},Target:[1},ReturnTo:{2},Mission:{3}".format(origin, target, returnTarget, msg) #set the message in a string format

        s.bind(('', 9999))

        s.sendto(message.encode('ascii'), ('<broadcast>', 9999))

        enterTime = int(time.time())
        while "-1" not in help:
            data = s.recvfrom(1024)
            help = str(data)
            if enterTime + 10 < int(time.time()):
                return False
        return True

    
