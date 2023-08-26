from random import *
from myRegistration import Registration
# import pandas as pd
# import openpyxl
import sqlite3
conn = sqlite3.connect('registration_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS Registers
          (name char(100),ID char(6))
          ''')
#using excel
print("Welcome to the registration panel")
noofentries = int(input("Number of entries you want to make: "))
# datalist = {}
# datalist['Name'] = []
# datalist['ID'] = []
x = 1
while x <= noofentries:
    # listofobjects = []
    nameofobj = input("Enter name of the object you want to register: ")
    newobject = Registration(nameofobj)
    idofobj= newobject.createID()
    #idofobj = newobject.getID()
    c.execute("""
    INSERT INTO Registers(name, ID)
    VALUES (?,?)
    """, (nameofobj, idofobj))
    conn.commit()
    print("data entered successfully")

    # datalist['Name'].append(nameofobj)
    # datalist['ID'].append(newobject.createID())
    # datalist[noofentries] = listofobjects
    x+=1

def get_data():
    with conn:
        c.execute("SELECT * FROM Registers")
        print(c.fetchall())

get_data()


# df = pd.DataFrame(datalist, columns=['Name', 'ID'])
# df.to_excel('RegistrationExcel.xlsx')





#trying sqlite3

#conn.commit()


# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE RegistrationFile (name VARCHAR(255), IDnumber VARCHAR(255))")

# conn.close()
# if(conn):
#     conn.close()
#     print("The SQLite3 connection now closed")