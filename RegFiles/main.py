from random import *
from myRegistration import Registration
import sqlite3
conn = sqlite3.connect('registration_database') # makes a new database if an existing one isn't given
mycursor = conn.cursor()

mycursor.execute('''
          CREATE TABLE IF NOT EXISTS Registers
          ( Name char(100),ID char(6))
          ''')
mycursor.execute('''
          CREATE TABLE IF NOT EXISTS PeopleRegisters
          ( Name char(100),Email char(100), Password char(8))
          ''')
def previous_customer():
    answer = input("Have you logged in before?(y/n): ")
    if answer == "y":
        name = input("Please enter your name: ")
        data=mycursor.execute('''SELECT * FROM PeopleRegisters''')
        mylist = []
        for row in data:
            mylist.append(row[0])
        print(mylist)
        x = False
        for i in mylist:
            if i == name:
                x = True
        return x
    elif answer == "n":
        user_login()

def user_login():
    print("Thank you for choosing our app")
    name = input("Please enter your name: ")
    email = input("Please enter email: ")
    password = input("Please enter password: ")
    mycursor.execute("""
    INSERT INTO PeopleRegisters(Name, Email, Password)
    VALUES (?,?,?)
    """, (name, email,password))

def enter_data(objectname, idofobject):
    mycursor.execute("""
    INSERT INTO Registers(Name, ID)
    VALUES (?,?)
    """, (objectname, idofobject))
    conn.commit()
    
# only repeats once after user registers for the first time
def first_entry():
    print("\nWelcome to the registration panel")
    noofentries = int(input("Number of entries you want to make: "))


    while noofentries > 0:
        nameofobj = input("Enter name of the object you want to register: ")
        newobject = Registration(nameofobj)
        idofobj= newobject.createID()
        enter_data(nameofobj,idofobj)
        noofentries-=1  
    
# when user is already logged in
def later_entries():
    print("\nWelcome Back :)")
    noofentries = int(input("Number of entries you want to make: "))
    while noofentries > 0:
        nameofobj = input("Enter name of the object you want to register: ")
        newobject = Registration(nameofobj)
        idofobj= newobject.createID()
        data=mycursor.execute('''SELECT * FROM Registers''')
        mylist = []
        x = False
        for row in data:
            mylist.append(row[0])
        for i in mylist:
            if i == nameofobj and x == False:
                print("object already Exists")
                x = True
                break
            elif x!=True  :
                enter_data(nameofobj,idofobj)
                break
        noofentries-=1




        
def getting_started():
    if previous_customer():
        later_entries()
    else:
        first_entry()

getting_started()


def get_data():
    with conn:
        mycursor.execute("SELECT * FROM Registers")
        print(mycursor.fetchall())
    with conn:
        mycursor.execute("SELECT * FROM PeopleRegisters")
        print(mycursor.fetchall())

get_data()



