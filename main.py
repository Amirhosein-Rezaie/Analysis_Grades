from tools.func import (
    check_database_first_time, run_command, start_database, press_enter_to_continue
)
from msvcrt import getwch

# varialbes
flag_first_time_run = check_database_first_time()

# funcs 
# # show the list of works 
def list_of_works() -> int:
    "show the list of works "
    
    print(
        """
        (1) --- students management
        (2) --- subjects management
        (3) --- grades managements
        (4) --- analysis grades
        """
    )
    print("Enter the number of work [1,4] : ", flush=True, end='')
    while True:
        try:
            number = int(getwch()); print(number)
            
            if number >= 1 and number <= 4:
                return number
        except:
            pass

# show the list of subworks base on list of works
def list_of_subworks(number_work:int):
    "show the list of subworks base on list of works"
    
    subworks = {
        1: ["(1) --- Add", "(2) --- Delete", "(3) --- Edit", "(4) --- Search"],
        2: ["(1) --- Add", "(2) --- Delete", "(3) --- Edit", "(4) --- Search"],
        3: ["(1) --- Add", "(2) --- Delete", "(3) --- Edit", "(4) --- Search"],
        4: ["(1) --- Avrg of student"],
    }

    # show the list of subworks
    print("\t\t" + "(0) --- Go back")
    for value in subworks[number_work]:
        print("\t\t" + value)

    print("Enter the number of subwork [0,4] : ", flush=True, end='')
    while True:
        try:
            number = int(getwch()); print(number)
            
            if number >= 0 and number <= 4:
                return number
        except:
            pass

# main of program
def main() -> None:
    "main of program"
    
    global flag_first_time_run
    
    while True:
    
        # check database exists for realise to the program ran first time
        if flag_first_time_run == True:
            start_database()
            print("Database created Successfully ... !")
            press_enter_to_continue()
            flag_first_time_run = False

        # get the number of work from user
        run_command(r"cls")
        code_work = list_of_works()
        code_subwork = list_of_subworks(code_work)
        
        if code_subwork == 0: continue
        
        press_enter_to_continue()
        
if __name__ == "__main__": main()
