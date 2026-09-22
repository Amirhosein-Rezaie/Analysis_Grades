from pickle import TRUE
from subprocess import run
from os.path import exists
from msvcrt import getwch

# run a command in cmd
def run_command(command:str) -> int:
    try:
        run(command, shell=True)
        return 0
    except:
        return 1
    
# check the program ran for first time or not
def check_database_first_time() -> bool:
    return not exists("./database.sqlite3")

# create the database and tables
def start_database() -> None:
    run_command(r"py database\start.py")

# the func that check enter pressed
def press_enter_to_continue() -> None:
    print("Press enter to continue ... ", end='', flush=True)
    
    while True:
        char = getwch()
        
        if repr(char) == repr('\r'): break
