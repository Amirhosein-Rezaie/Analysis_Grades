from tools.func import (
    check_database_first_time, start_database, press_enter_to_continue
)

# varialbes
flag_first_time_run = check_database_first_time()

# main of program
def main() -> None:
    global flag_first_time_run
    
    while True:
    
        if flag_first_time_run == True:
            start_database()
            print("Database created Successfully ... !")
            press_enter_to_continue()
            flag_first_time_run = False

if __name__ == "__main__": main()
