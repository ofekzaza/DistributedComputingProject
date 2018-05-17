import communicator

ci = communicator.Communicator()

ci.send('1','1','1','1')
print("good")
print(str(ci.recive('1')))