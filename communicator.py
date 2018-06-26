import socket


class Communicator():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # creating the socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # added in order to fix the bug the may accure
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def __init__(self, port: int = 9999):
        if port > 9999 or port < 0:
            raise ValueError('mate, are you retard? you gave false port, THE NEW PORT IS 9999')
            port = 9999
        self.s.bind(('', port))

    def send(self, origin: str, target: str, returnTarget: str, msg: str,state: int = 2):
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target
        # mission : what target needs to do
        # state : to which state machine target needs to change
        "the function is sending data "
        message: str = "Origin:"+origin+",Target:"+target+",ReturnTo:"+returnTarget+",Mission:"+msg+",State:"+state #set the message in a string format
        self.s.sendto(message.encode('ascii'), ('<broadcast>', 9999))
        return origin, target, returnTarget, msg, state

    def receive(self, listener: str):
        "function is responsible of reciving data from a broadcast"
        data, address = self.s.recvfrom(1024)
        data = str(data, 'utf-8')
        if ("Target:"+listener) not in data:
            return -1
        self.s.sendto(("Thanks"+listener).encode('ascii'), ('<broadcast>', 9999))

        help = data.split("Origin:")
        helper = help[1].split(",Target:")
        origin = helper[0]
        help = helper[1].split(",ReturnTo:")
        target = help[0]
        if target != listener:
            assert "Error, communication read wrong message"
        helper = help[1].split(",Mission:")
        returnTarget = helper[0]
        help = helper.split(",State:")
        mission = help[0]
        state = help[1]
        return origin, target, returnTarget, mission, state
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target
        # mission : what target needs to do
        # state : to which state machine target needs to change

    def waitReceive(self, listener: str):
        "listener is waiting for a broadcast for him"
        data = None
        while data is None:
            data, address = self.s.recvfrom(1024)

        "broadcast have been received by listener"

        data = str(data, 'utf-8')
        if ("Target:" + listener) not in data:
            return -1
        self.s.sendto(("Thanks" + listener).encode('ascii'), ('<broadcast>', 9999))

        helps = data.split("Origin:")
        helper = help[1].split(",Target:")
        origin = helper[0]
        helps = helper[1].split(",ReturnTo:")
        target = help[0]

        if target != listener:
            assert "Error, communication read wrong message"

        helper = help[1].split(",Mission:")
        returnTarget = helper[0]
        helps = helper.split(",State:")
        mission = help[0]
        state = help[1]

        return origin, target, returnTarget, mission, state
        # origin : who send the message
        # target : who receives the message
        # returnTarget : who need to receive a message from target
        # mission : what target needs to do
        # state : to which state machine target needs to change


    def __del__(self):
        self.s.close()
        print('Communicator died, RIP')





