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

    def send(self, origin: str, target: str, returnTarget: str, msg: str) -> bool:
        "the function is sending data "
        message: str = "Origin:"+origin+",Target:"+target+",ReturnTo:"+returnTarget+",Mission:"+msg #set the message in a string format
        self.s.sendto(message.encode('ascii'), ('<broadcast>', 9999))
        return True

    def recive(self, listener: str)-> str:
        "function is responsible of reciving data"
        data, address = self.s.recvfrom(1024)
        data = str(data, 'utf-8')
        if ("Target:"+listener) not in data:
            return -1
        self.s.sendto(("ThanKs"+listener).encode('ascii'), ('<broadcast>', 9999))
        return data

    def __del__(self):
        self.s.close()
        print('Communicator died, RIP')





