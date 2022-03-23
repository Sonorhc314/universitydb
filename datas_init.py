# importing required libraries
import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database='University',
)

# preparing a cursor object
cursorObject = dataBase.cursor(buffered=True)

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
                   Password Varchar(20),
                   GPA DECIMAL(5,2) CHECK(101>GPA),
                   FOREIGN KEY (FacultyID) REFERENCES University(FacultyID)  
                   )"""


cursorObject.execute(university)
cursorObject.execute(faculty1)
cursorObject.execute(faculty2)
cursorObject.execute(student)

cursorObject.execute("INSERT University(Faculty) VALUES('Mathematics'),('Comp Science')")
cursorObject.execute("INSERT Faculty1(Spec) VALUES('Pure'),('Software')")
cursorObject.execute("INSERT Faculty2(Spec) VALUES('AI'),('Data science')")


cursorObject.execute("INSERT Student(Name, Surname, FacultyID, SpecID, Password, GPA) "
                     "VALUES('Mari','Lee',1,1,'1111',83)")

cursorObject.execute("INSERT Student(Name, Surname, FacultyID, SpecID, Password, GPA) "
                     "VALUES('Dove','Loff',1,1, 'password', 95)")
cursorObject.execute("INSERT Student(Name, Surname, FacultyID, SpecID, Password, GPA) "
                     "VALUES('Maeria','Stotskaya',1,2, 'apple', 80)")
cursorObject.execute("INSERT Student(Name, Surname, FacultyID, SpecID, Password, GPA) "
                     "VALUES('Alisa','Lee',2,1, '1234', 60)")

dataBase.commit()