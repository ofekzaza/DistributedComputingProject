import socket
import time

class Communicator():
    s:socket
    port:int
    name: str = ""
    user:str

    def __init__(self, p, name = None,  user = "master"):
        if name is not None:
            self.name = name
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # creating the socket
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # added in order to fix the bug the may accure
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        port = p
        if port > pow(2,16)-1 or port < 0:
            print('mate, are you retard? you gave false port, THE NEW PORT IS 9999')
            port = 9999
        self.s.bind(('', int(port)))
        self.port = port
        self.user = user

    def send(self, origin: str, target: str, returnTarget: str, msg: str,state: int = 1)-> [str]: #str *5
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target, -1 is to the origin, -2 is not returning data
        # mission : what target needs to do
        # state : to which state machine target needs to change
        "the function is sending data "
        message = "Origin:"+str(origin)+",Target:"+str(target)+",ReturnTo:"+str(returnTarget)+",Mission:"+str(msg)+",State:"+str(state) #set the message in a string format
        self.s.sendto(message.encode('ascii'), ('<broadcast>', self.port))
        return origin, target, returnTarget, msg, state

    def receive(self, listener: str, times: int = 1)-> [str]: #str * 5
        """dont use times"""
        """function is responsible of reciving data from a broadcast"""
        if listener is None:
            return False
        data, address = self.s.recvfrom(1024)
        data = str(data, 'utf-8')
        if (str("Target:"+str(listener))) not in data:
            if times == 1:
                if self.kindOfEcho(data, listener) is not None:
                    time.sleep(0.000000001)
                    print("Port number: '%s' which listen by listener: '%s' read echo ,Rereading. read an echo" % (self.port, listener))
                    return self.receive(listener, times+1)
                elif self.checkChange(data):
                    return self.port, self.port, self.port, self.port, self.port
                if (str("Origin:"+listener)) in data:
                    print("%s read its own message, lol" % str(listener))
                    return None, None, None, None, None
                print("Port number: '%s' which listen by listener: '%s' got this message: '%s'. Rereading, why: gen" % (self.port, listener, data))
                time.sleep(0.000000001)
                return self.receive(listener, times + 1)
            return None, None, None, None, None

        help = data.split("Origin:")
        helper = help[1].split(",Target:")
        origin = helper[0]
        help = helper[1].split(",ReturnTo:")
        target = help[0]

        if str(target) != str(listener): # Listener is not target
            self.s.sendto(("Communication Error which send by %s to %s" %(origin, listener)).encode('ascii'), ('<broadcast>', self.port))#Echo
            raise ValueError("Error, communication read wrong message")

        helper = help[1].split(",Mission:")
        returnTarget = helper[0]
        help = helper[1].split(",State:")
        mission = help[0]
        state = help[1]

        """echo"""
        self.sendEcho(origin, listener)

        return origin, target, returnTarget, mission, state
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target
        # mission : what target needs to do
        # state : to which state machine target needs to change

    def waitReceive(self, listener) -> [str]: #str * 5
        """listener is waiting for a broadcast for him, don't use times - valuable exist to serve the function"""
        data = None
        d:str
        while str("Target:"+str(listener)) not in str(data):
            if data is not None:
                print(str(data))
                d = str(data, 'utf-8')
                if self.checkChange(d):
                    return self.port, self.port, self.port, self.port, self.port
            data, address = self.s.recvfrom(1024)
            time.sleep(0.0000000001)
        data = str(data, 'utf-8')

        #print(data)
        help = data.split("Origin:")
        helper = help[1].split(",Target:")
        origin = helper[0]
        help = helper[1].split(",ReturnTo:")
        target = help[0]
        if str(target) != str(listener):  # Listener is not target
            self.s.sendto(("Communication Error which send by %s to %s" % (origin, listener)).encode('ascii'),
                          ('<broadcast>', self.port))  # Echo
            raise ValueError("Error, communication read wrong message")

        helper = help[1].split(",Mission:")
        returnTarget = helper[0]
        help = helper[1].split(",State:")
        mission = help[0]
        state = help[1]

        """echo"""
        self.sendEcho(origin, listener)

        return origin, target, returnTarget, mission, state
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target
        # mission : what target needs to do
        # state : to which state machine target needs to change

    def toString(self) -> str:
        return "communicator port "+str(self.port)

    def readEcho(self, target) -> bool:
        """chreck if communicator read an echo from target"""
        data = self.s.recvfrom(1024)
        if data is not None:
            if (",from:%s" %(target)) in str(data) and "Thanks:" in str(data):
                return True
        return False

    def kindOfEcho(self, data, target) -> bool:
        """Function get the message and the listener and return True is the message is an Echo @sendEcho"""
        if data is not None:
            if 'ECHO' in data:
                if (",from:%s" %target) in str(data) and "Thanks:" in str(data):
                    return "Communication.receive ECHO"
                return "ECHO"
        return None

    def sendEcho(self,origin, listener):
        """This Function get the origin of a message and the one who got it, and send an Echo to the same port
        Echo follows this structure:'ECHOThanks:%origin,from:%listener' % sign a valuable """
        if str(origin) is not None and str(listener) is not None:
            self.s.sendto(("ECHOThanks:%s,from:%s" % (origin, listener)).encode('ascii'), ('<broadcast>', self.port))
            return True
        raise ValueError("Illegal Echo values")

    def kill(self, who):
        """Order the death of a worker"""
        if self.user == 'worker':
            print("worker can't kill other workers")
            return False
        self.s.sendto(("KILL"+str(who)).encode(), ('<broadcast>', self.port))
        return True

    def setPort(self, port):
        """Does not recommended to do, change the port of the communication"""
        self.s.sendto(("ChangeNewPort"+str(port)).encode(), ('<broadcast>', self.port))
        print("Communication port have changed from "+self.port+"  to "+port)
        self.port = port
        return True

    def checkChange(self, data:str):
        """check if data say to the communicator to change it current port"""
        if data is not None and "ChangeNewPort" in data:
            port = data.split("ChangeNewPort")[0]
            if port > pow(2, 16) - 1 or port < 0:
                print('mate, are you retard? you gave false port')
                return False
                port = 9999
            self.s.close()
            self.s = None
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # creating the socket
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # added in order to fix the bug the may accure
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.s.bind(('', int(port)))
            self.port = port
            return True

    def listen(self, who):
        """function for workers to check if they suppose to die"""
        data = self.s.recvfrom(1024)
        data = str(data)
        if  str("KILL"+str(who)) in data:
            self.deathEcho(who)
            return True
        return False

    def deathEcho(self, who):
        """before death worker send an Echo to say that he will be Dead"""
        self.s.sendto(("TheSoundOfSilenceIsLikeTheSoundOfWorker"+str(who)).encode(), ('<broadcast>', self.port))
        return True

    def __del__(self):
        self.s.close()
        print('Communicator %s died, RIP' % self.name)
