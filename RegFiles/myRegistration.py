from random import *
class Registration:
    def __init__(self,name):
        self.name = name
        self.id = ""

    def createID(self):
        for i in range(0,6):
            y = randint(0,10)
            self.id += str(y)
        return self.id
    def getID(self):
            print(self.id)

# if __name__=="__main__":
#     print("Welcome to the registration panel")
#     nameofobj = input("Enter name of the object you want to register: ")
#     newobject = Registration(nameofobj)
#     newobject.createID()
#     newobject.getID()