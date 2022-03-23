import datas_init as data
import menu_user as user

def menu():
    print("""Choose an action\n 
            1)Create a new account\n
            2)See all Faculties\n
            3)See all students\n
            4)Log in\n
            ENTER "q" TO QUIT
            """)


def fetcher():
    myresult = data.cursorObject.fetchall()
    for x in myresult:
        print(x)


choice = 0


while(choice != 'q'):
    menu()
    choice = input('1-4 : ')
    if choice == '1':
        name = input("Enter Name: ")
        sur = input("Enter Surname: ")
        facult = int(input("Enter your FacultyID(1,2): "))
        spec = int(input("Enter your SpecID(1,2): "))
        passw = input("Enter your Password: ")
        gpa = int(input("Enter your GPA(from 60 to 100): "))
        insert_st = f"INSERT Student(Name, Surname, FacultyID, SpecID, Password, GPA) " \
                    f"VALUES('{name}','{sur}',{facult},{spec},'{passw}',{gpa})"
        data.cursorObject.execute(insert_st)
        data.dataBase.commit()
    elif choice == '2':
        data.cursorObject.execute("SELECT * FROM UNIVERSITY")
        fetcher()
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=1")
        records = data.cursorObject.fetchall()
        print('1)', records[0], 'Students')
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=2")
        records = data.cursorObject.fetchall()
        print("2)", records[0], 'Students')
    elif choice == '3':
        data.cursorObject.execute("SELECT ID, Name, Surname, FacultyID, University.Faculty, "
                                  "Student.SpecID, "
                                  "faculty1.Spec FROM STUDENT INNER JOIN faculty1 USING(FacultyID, SpecID)"
                                  "INNER JOIN University USING(FacultyID) " 
                                  "UNION "
                                  "SELECT ID, Name, Surname, FacultyID, University.Faculty, "
                                  "Student.SpecID, "
                                  "faculty2.Spec FROM STUDENT INNER JOIN faculty2 USING(FacultyID, SpecID) "
                                  "INNER JOIN University USING(FacultyID) "
                                  "ORDER BY 4,6,3")
        fetcher()
    elif choice == '4':
        id = int(input("Your ID(check in 'see all students'): "))
        passw1 = input("Password: ")
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=1")
        records_count = data.cursorObject.fetchall()
        id_1 = int(records_count[0][0])
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=2")
        records_count = data.cursorObject.fetchall()
        id_2 = int(records_count[0][0])
        id_all = id_1+id_2
        if(id_all >= id):
            data.cursorObject.execute(f"SELECT Password FROM Student WHERE ID = {id}")
            pass_sql = data.cursorObject.fetchone()[0]
            if(pass_sql == passw1):
                data.cursorObject.execute(f"SELECT Name, Surname FROM Student WHERE ID = {id}")
                records_log = data.cursorObject.fetchall()
                name_log = records_log[0][0]
                sur_log = records_log[0][1]
                print("You are logged as", name_log, sur_log)
            else:
                print("Either your ID or your password is invalid!")
        else:
            print("Either your ID or your password is invalid!")
    else:
        continue


# disconnecting from server

data.dataBase.close()