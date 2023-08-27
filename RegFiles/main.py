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
    answer = input("Have you logged in before?(y/n)")
    if answer == "y":
        name = input("Please enter your name: ")
        data=mycursor.execute('''SELECT * FROM PeopleRegisters''')
        mylist = []
        for row in data:
            mylist.append(row[0])
        print(mylist)
        for i in mylist:
            if i == name:
                return True
            else :
                return False
        else:
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
    # data=mycursor.execute('''SELECT * FROM PeopleRegisters''')
    # mylist = []
    # for row in data:
    #     mylist.append(row[0])
    # print(mylist)
    # for i in mylist:
    #     if i == name  and len(mylist) != 1:
    #         return True
    #     else :
    #         return False

def enter_data(objectname, idofobject):
    mycursor.execute("""
    INSERT INTO Registers(Name, ID)
    VALUES (?,?)
    """, (objectname, idofobject))
    conn.commit()
    
# only repeats once after user registers for the first time
def first_entry():
    print("Welcome to the registration panel")
    noofentries = int(input("Number of entries you want to make: "))


    while noofentries > 0:
        nameofobj = input("Enter name of the object you want to register: ")
        newobject = Registration(nameofobj)
        idofobj= newobject.createID()
        enter_data(nameofobj,idofobj)
        noofentries-=1  
    
# when user is already logged in
def later_entries():
    print("Welcome Back :)")
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



# using excel
# import pandas as pd
# import openpyxl
# datalist = {}
# datalist['Name'] = []
# datalist['ID'] = []
#listofobjects = []
# datalist['Name'].append(nameofobj)
# datalist['ID'].append(newobject.createID())
# datalist[noofentries] = listofobjects
# df = pd.DataFrame(datalist, columns=['Name', 'ID'])
# df.to_excel('RegistrationExcel.xlsx')





#trying sqlite3
#conn.commit()
# mycursor = mydb.cursor()
#db = sqlite3.connect("enternameofdatabase")
# mycursor.execute("CREATE TABLE RegistrationFile (name VARCHAR(255), IDnumber VARCHAR(255))")
# conn.close()
# if(conn):
#     conn.close()
#     print("The SQLite3 connection now closed")
# def table_exists():
#     global countval
#     mycursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Registers';")
#     if mycursor.fetchall() != None:
#         countval +=1