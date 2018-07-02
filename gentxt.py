import sys
import random
another= True

abc = "abcdefghijklmnopqrstuvwxyz"
name:str
type:str
file = None
a:str

s = input("special so enter yes")

if s == 'yes':
    for i in range(0, 10):
        file = open(str(str(i)+'.txt'), "w")
        for i in range(0, 100000):
            file.write(abc[random.randint(0, 25)])

        file.close()
    sys.exit()

while another:
    name = input("what is the name of the file? ")
    type = input("what is the type of the file? ")
    file = open(str(name+"."+type), "w")

    for i in range(0, 100000):
        file.write(abc[random.randint(0,25)])

    file.close()

    a = input("continue? ")
    if a == 'y' or a == 'yes' or a == 'Yes' or a == 'True' or a == 'hye':
        another = True
    else:
        another = False
