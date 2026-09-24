from database.Database import Database
from msvcrt import getwch
from tools.func import check_number_greater_zero, press_enter_to_continue, table

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
        # try to make int the unit
        unit = input("Enter the unit of new subject : ")
        
        if check_number_greater_zero(unit, True):
            break
        else:
            print("Please enter number greater that zero for new unit ... !")
            press_enter_to_continue
    
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

# edit the subject by code
def edit_subject() -> int:
    "edit the subject by code"
    
    global subject
    
    # get input from user
    code = input("Enter the code of subject : ")
    
    flag_find = False
    
    # try to find the subject
    try:
        data = subject.Get_Query(
            f"SELECT * FROM subjects WHERE code='{code}'", fetch_result=True
        )
        
        if data != []:
            table(data, columns)
            flag_find = True
        else:
            print(f"The Subject with {code} code not found ... !")
            return 1
    except:
        print("Problem in searching for subject ... !")
        return 1

    # try to edit the subject
    if flag_find:
        # get input the new data
        new_title = input("Enter the new title : ")
        new_code = input("Enter the new code : ")
        new_unit = 0
        while True:
            new_unit = input("Enter the new unit : ")
            if check_number_greater_zero(new_unit, True):
                break
            else:
                print("Please enter number greater that zero for new unit ... !")
                press_enter_to_continue
                
        # try to edit
        try:
            subject.Get_Query(
                f"UPDATE subjects SET title='{new_title}', code='{new_code}', unit='{new_unit}' WHERE code='{code}'"
            )
            print("The subject edited Successfuly ... !")
            return 0
        except:
            print("Editing the subject Failed ... !")
            return 1
