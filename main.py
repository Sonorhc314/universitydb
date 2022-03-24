import datas_init as data


def fetcher():
    myresult = data.cursorObject.fetchall()
    for x in myresult:
        print(x)


def tuition(gpa_t):
    if gpa_t >= 80:
        print("You have tuition")
    else:
        print(f"No tuition, your GPA({gpa_t}) has to be {80-gpa_t} points higher")


choice, flag = 0, 0
facult_log, gpa_log, id_log = 1, 60, 0


def menu():
    print("""
            Choose an action\n 
            1)Create a new account\n
            2)See all Faculties\n
            3)See all students\n
            4)Find a student""")
    if flag == 1:
        print("""
            5)See your faculty's rating list\n
            6)Check if you have a tuition\n
            7)Update password\n
            8)Log out
            """)
    else:
        print("""
            5)Log in\n
                """)
    print("""
            To receive tuition student's gpa has to be >= 80\n
            ENTER 'q' TO QUIT""")


while choice != 'q':
    menu()
    if flag == 0:
        choice = input('1-5 : ')
    else:
        choice = input('1-8 : ')
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
        print('1)', records[0][0], 'Students')
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=2")
        records = data.cursorObject.fetchall()
        print("2)", records[0][0], 'Students')
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
        name_find = input("Name: ")
        sur_find = input("Surname: ")
        data.cursorObject.execute(f"SELECT ID, Name, Surname, FacultyID, SpecID FROM Student "
                                  f"WHERE Name = '{name_find}' AND Surname = '{sur_find}'")
        fetcher()
    elif choice == '5' and flag == 0:
        id_log = int(input("Your ID(check in 'see all students'): "))
        passw1 = input("Password: ")
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=1")
        records_count = data.cursorObject.fetchall()
        id_1 = records_count[0][0]
        data.cursorObject.execute("SELECT COUNT(*) FROM Student WHERE FacultyID=2")
        records_count = data.cursorObject.fetchall()
        id_2 = records_count[0][0]
        id_all = id_1+id_2
        if id_all >= id_log:
            data.cursorObject.execute(f"SELECT Password FROM Student WHERE ID = {id_log}")
            pass_sql = data.cursorObject.fetchone()[0]
            if pass_sql == passw1:
                data.cursorObject.execute(f"SELECT Name, Surname, FacultyID, GPA FROM Student WHERE ID = {id_log}")
                records_log = data.cursorObject.fetchall()
                name_log = records_log[0][0]
                sur_log = records_log[0][1]
                facult_log = records_log[0][2]
                gpa_log = records_log[0][3]
                print("You are logged as", name_log, sur_log)
                flag = 1
            else:
                print("Either your ID or your password is invalid!")
        else:
            print("Either your ID or your password is invalid!")
    elif choice == '5' and flag == 1:
        data.cursorObject.execute("SELECT ID, Name, Surname, GPA, FacultyID, University.Faculty, "
                                  "Student.SpecID, "
                                  f"faculty{facult_log}.Spec FROM STUDENT "
                                  f"INNER JOIN faculty{facult_log} USING(FacultyID, SpecID)"
                                  "INNER JOIN University USING(FacultyID)"
                                  "ORDER BY GPA")
        fetcher()
    elif choice == '6' and flag == 1:
        print("Your tuition status: ", tuition(gpa_log))
    elif choice == '7' and flag == 1:
        new_pass = input("Your new password:")
        data.cursorObject.execute(f"UPDATE Student SET Password = {new_pass} WHERE ID = {id_log}")
        print("Your password was updated")
    elif choice == '8' and flag == 1:
        flag = 0
        print("Logged out successfully")
    else:
        continue


# disconnecting from server

data.dataBase.close()
