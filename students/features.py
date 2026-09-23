from database.Database import Database
from tools.func import (
    splitter_line_table, UP_POSITION_NEW_LINE_TABLE, MID_POSITION_NEW_LINE_TABLE, DN_POSITION_NEW_LINE_TABLE
)

# variables
student = Database("database.sqlite3")


# functions as tools
def show_one_student(student_data):
    "a function that show one student in the table"
    data = student_data
    
    splitter_line_table(UP_POSITION_NEW_LINE_TABLE)
        
    print(f"{'ID':<5} | {'firstname':<15} | {'lastname':<15} | {'national_code':<15}")
    splitter_line_table(MID_POSITION_NEW_LINE_TABLE)
    
    print(f"{data[0]:<5} | {data[1]:<15} | {data[2]:<15} | {data[3]:<15}")
    
    splitter_line_table(DN_POSITION_NEW_LINE_TABLE)


# add student
def add_student() -> int:
    "function add student to database"
    
    global student
    
    # get the information of student
    firstname = input("Enter the firstname of student : ")
    lastname = input("Enter the lastname of student : ")
    code =  input("Enter the nationl code of student : ")
    
    # try to add the new student
    try:
        student.Get_Query(
            f"INSERT INTO students (firstname, lastname, code) VALUES ('{firstname}', '{lastname}', '{code}')"
        )

        print(f"Adding {firstname} {lastname} Successfully Done ... !", flush=True)
    
        return 0
    
    except:
        print("Adding new student Failed ... !", flush=True)
        
        return 1

# get all of students in the database
def show_all_students():
    "get all of students in the database"
    
    global student
    
    # get query to the database 
    rows = student.Get_Query("SELECT * FROM students", fetch_result=True)
    
    # show the title or template of table of students 
    splitter_line_table(new_line_position=UP_POSITION_NEW_LINE_TABLE)
    print(f"{'#':<5} | {'Firstname':<15} | {'Lastname':<15} | {'National Code':<15}")
    
    splitter_line_table(new_line_position=MID_POSITION_NEW_LINE_TABLE)

    # show the data in the table
    row_number = 1
    for row in rows:
        print(f"{row_number:<5} | {row[1]:<15} | {row[2]:<15} | {row[3]:<15}")
        row_number += 1
        
    splitter_line_table(new_line_position=DN_POSITION_NEW_LINE_TABLE)


# delete a specific student by national code
def delete_student():
    "delete a specific student by national code"
    
    global student
    
    # get input from user
    code = input("Enter the national code of student that you want to delete : ")
    
    # try to found the student that is going to delete
    try:
        deleted_student = student.Get_Query(f"SELECT * FROM students WHERE code='{code}'", fetch_result=True)[0]
    except IndexError:
        print("The student not found ... !")
        
        return 1 
    
    # try to delete the student by the nationl code
    try:
        student.Get_Query(f"DELETE FROM students WHERE code='{code}'")
        
        print(f"{deleted_student[1]} {deleted_student[2]} student deleted Successfully ... !")
        
        return 0
        
    except:
        print(f"Deleting {deleted_student[1]} {deleted_student[2]} student failed ... !")
        
        return 1

# edit the student data by using nationl code
def edit_student():
    "edit the student data by using nationl code"
    
    global student
    
    # get input natioal code from the user
    code = input("Enter the nationl code : ")
    
    # try to find the student that in going to edit
    data = None
    
    try:
        data = student.Get_Query(f"SELECT * FROM students WHERE code='{code}'", fetch_result=True)[0]
    except:
        print("The student not found ... !")
        return 1
    
    # show the data of student in a table
    show_one_student(data)
    
    # get new data from the user
    new_firstname = input(f"Enter the new firstname of {data[1]} : ")
    new_lastname = input(f"Enter the new lastname of {data[2]} : ")
    new_code = input(f"Enter the new nationl_code of {data[3]} : ")
    
    # try to update data of the student in the database
    try:
        student.Get_Query(
            f"""UPDATE students 
                SET firstname='{new_firstname}', lastname='{new_lastname}', code='{new_code}'
                WHERE code='{code}'
                """
        )
        print("Student updated Successfuly ... !")
        
        return 0
        
    except:
        print("Updating student failed ... !")
        
        return 1

# search the student 
def search_student() -> None:
    "search the student "
    
    code = input("Enter the national code : ")
    
    # try to find the student that in going to edit
    data = None
    
    try:
        data = student.Get_Query(f"SELECT * FROM students WHERE code='{code}'", fetch_result=True)[0]
    except:
        print("The student not found ... !")
        return 1
    
    # show the data of student in a table
    show_one_student(data)
