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
