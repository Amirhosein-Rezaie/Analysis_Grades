from pickle import TRUE
from subprocess import run
from os.path import exists
from msvcrt import getwch

UP_POSITION_NEW_LINE_TABLE = 1
MID_POSITION_NEW_LINE_TABLE = 2
DN_POSITION_NEW_LINE_TABLE = 3

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

# the function for show a splitter line
def splitter_line() -> None:
    "show a splitter line"
    
    print("-" * 80)

# show a splitter line for table. the arg is position of line that can manage by the const in this module
def splliter_line_table(new_line_position:int) -> None:
    "show a splitter line for table. the arg is position of line that can manage by the const in this module"
    
    if new_line_position == 1: print("\n" + "-" * 60)
    
    elif new_line_position == 2: print("-" * 60)
    
    else: print("-" * 60 + "\n")
