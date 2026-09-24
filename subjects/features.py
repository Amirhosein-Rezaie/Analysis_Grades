from database.Database import Database
from tools.func import press_enter_to_continue, table

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
                press_enter_to_continue()
        except:
            print("Please enter unit as a number ... ")
            press_enter_to_continue()
    
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
