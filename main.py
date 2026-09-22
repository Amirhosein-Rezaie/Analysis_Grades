from tools.func import (
    check_database_first_time, run_command, start_database, press_enter_to_continue
)
from msvcrt import getwch

# varialbes
flag_first_time_run = check_database_first_time()

# funcs 
def list_of_works() -> int:
    print(
        """
        (1) --- students management
        (2) --- subjects management
        (3) --- grades managements
        (4) --- analysis grades
        (5) --- reporting
        """
    )
    print("Enter the number of work [1,5] : ", flush=True, end='')
    while True:
        try:
            number = int(getwch())
            
            if number >= 1 and number <= 5:
                return number
        except:
            pass

# main of program
def main() -> None:
    global flag_first_time_run
    
    while True:
    
        if flag_first_time_run == True:
            start_database()
            print("Database created Successfully ... !")
            press_enter_to_continue()
            flag_first_time_run = False

        run_command(r"cls")
        code_work = list_of_works()
        
if __name__ == "__main__": main()
