import communicator

com = communicator.Communicator(9999)

com.send('a','a','a','a')

type: str = -1

print(com.waitRecive('a'))