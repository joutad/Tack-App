from random import *
class Registration:
    def __init__(self,name):
        #self.mydict = {}
        self.name = name
        self.id = ""

    def createID(self):
        # if self.name not in self.mydict:
        for i in range(0,6):
            y = randint(0,10)
            self.id += str(y)
        return self.id
            #self.mydict[self.name] = self.id
    def getID(self):
        # if self.name in self.mydict:
            print(self.id)
        # else:
        #     print("Not registered")

# if __name__=="__main__":
#     print("Welcome to the registration panel")
#     nameofobj = input("Enter name of the object you want to register: ")
#     newobject = Registration(nameofobj)
#     newobject.createID()
#     newobject.getID()