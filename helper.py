import Comunication.Comunicator

ci = Comunication.Comunicator.Comunicatora()

ci.send('1','1','1','1')
print("good")
print(str(ci.recive('1')))