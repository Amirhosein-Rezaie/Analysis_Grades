from database.Database import Database
from msvcrt import getwch
from tools.func import table

# variables
subject = Database("database.sqlite3")
columns = ['title', 'code', 'unit']

# # functions of features
# add a new subject
def add_subject() -> None:
    "add a new subject"
    
    # variables
    global subject
    
    # get input from the user
    title = input("Enter the title of new subject : ")
    code = input("Enter the code of new subject : ")
    
    unit = 0
    while True:
        try: # try to make int the unit
            unit = int(input("Enter the unit of new subject : "))
            
            if unit > 0:
                break 
            else: 
                print("Please enter unit greater that zero ...")
        except:
            print("Please enter unit as a number ... ")
    
    # try to add a new subject
    try:
        subject.Get_Query(
            f"INSERT INTO subjects (title, code, unit) VALUES('{title}', '{code}', {unit})"
        )
        print(f"Adding '{title}' Successfuly Done ... !")
        return 0
    except:
        print("Adding new subject Failed ... !")
        return 1

# show all subjects in a table
def show_all_subjects() -> None:
    "show all subjects in a table"
    
    global subject
    
    rows = subject.Get_Query("SELECT * FROM subjects", fetch_result=True)
    
    table(rows, columns)

# delete subjects by code
def delete_subject() -> int:
    "delete subjects by code"
    
    global subject
    
    # get inptut
    code = input("Enter the code of subject : ")
    
    flag_delete = False
    title_sbj = None
    
    # try to find subject and get validation of deletion
    try:
        # search the subject
        data = subject.Get_Query(
            f"SELECT title FROM subjects WHERE code='{code}'", fetch_result=True
        )
        
        # check found or not
        if data != []:
            title_sbj = data[0][0]
            
            # get validation to delete the subject
            print(f"Do you want to delete {title_sbj} (y,n): ", end='', flush=True)
            while True:
                char = getwch()
                if char in ['y', 'n']: print(char); break
                    
            flag_delete = char == 'y'
        else:
            print(f"The Subject with {code} code not found ... !")
            return 1
    except:
        print("Problem in searching for subject ... !")
        return 1

    # try to delete the subject
    if flag_delete:
        try:
            subject.Get_Query(f"DELETE FROM subjects WHERE code='{code}'")
            print(f"{title_sbj} deleted Successfuly ... !")
            return 0
        except:
            print("Deleting the subject Failed ... !")
            return 1
    else:
        print(f"You canceled the deleting {title_sbj} ... !")
        return 1
