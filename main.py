# importing required libraries
import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database='University',
)

# preparing a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute('DROP TABLE if exists Student')
cursorObject.execute('DROP TABLE if exists Faculty1')
cursorObject.execute('DROP TABLE if exists Faculty2')
cursorObject.execute('DROP TABLE if exists University')

university = """CREATE TABLE UNIVERSITY (
                   FacultyID INT AUTO_INCREMENT PRIMARY KEY,
                   Faculty ENUM('Mathematics', 'Comp Science') UNIQUE
                   )"""

faculty1 = """CREATE TABLE Faculty1 (
                   SpecID INT AUTO_INCREMENT PRIMARY KEY,
                   Spec ENUM('Pure','Software') UNIQUE,
                   FacultyID INT DEFAULT 1,
                   FOREIGN KEY (FacultyID) REFERENCES University(FacultyID)
                   )"""

faculty2 = """CREATE TABLE Faculty2 (
                   SpecID INT AUTO_INCREMENT PRIMARY KEY,
                   Spec ENUM('AI','Data science') UNIQUE,
                   FacultyID INT DEFAULT 2,
                   FOREIGN KEY (FacultyID) REFERENCES University(FacultyID)  
                   )"""


student = """CREATE TABLE Student(
                   ID INT AUTO_INCREMENT PRIMARY KEY,
                   Name Varchar(30) NOT NULL,
                   Surname Varchar(30) NOT NULL,
                   FacultyID INT,
                   SpecID INT,
                   FOREIGN KEY (FacultyID) REFERENCES University(FacultyID)  
                   )"""


cursorObject.execute(university)
cursorObject.execute(faculty1)
cursorObject.execute(faculty2)
cursorObject.execute(student)

cursorObject.execute("INSERT University(Faculty) VALUES('Mathematics'),('Comp Science')")
cursorObject.execute("INSERT Faculty1(Spec) VALUES('Pure'),('Software')")
cursorObject.execute("INSERT Faculty2(Spec) VALUES('AI'),('Data science')")
name = input("Enter Name: ")
sur = input("Enter Surname: ")
facult = int(input("Enter your FacultyID(1,2): "))
spec = int(input("Enter your SpecID(1,2): "))
insert_st = f"INSERT Student(Name, Surname, FacultyID, SpecID) VALUES('{name}','{sur}',{facult},{spec})"
cursorObject.execute(insert_st)

#cursorObject.execute("INSERT Student(Name, Surname, FacultyID, SpecID) VALUES('Alisa','Lee',1,1)")
dataBase.commit()

#cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()