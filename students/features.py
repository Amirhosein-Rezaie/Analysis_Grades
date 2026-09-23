from database.Database import Database

# variables
student = Database("database.sqlite3")

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
def get_all_students():
    "get all of students in the database"
    
    global student
    
    # get query to the database 
    rows = student.Get_Query("SELECT * FROM students", fetch_result=True)
    
    # show the title or template of table of students 
    print("\n" + "-" * 60)
    print(f"{'ID':<5} | {'Firstname':<15} | {'Lastname':<15} | {'National Code':<15}")
    print("-" * 60)

    # show the data in the table
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<15} | {row[3]:<15}")
        
    print("-" * 60 + "\n")


# delete a specific student by national code
def delete_student():
    "delete a specific student by national code"
    
    global student
    
    code = input("Enter the national code of student that you want to delete : ")
    
    try:
        deleted_student = student.Get_Query(f"SELECT * FROM students WHERE code='{code}'", fetch_result=True)[0]
    except IndexError:
        print("The student not found ... !")
        
        return 1 
    
    try:
        student.Get_Query(f"DELETE FROM students WHERE code='{code}'")
        
        print(f"{deleted_student[1]} {deleted_student[2]} student deleted Successfully ... !")
        
        return 0
        
    except:
        print(f"Deleting {deleted_student[1]} {deleted_student[2]} student failed ... !")
        
        return 1
    