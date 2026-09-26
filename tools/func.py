from subprocess import run
from os.path import exists
from msvcrt import getwch

UP_POSITION_NEW_LINE_TABLE = 1
MID_POSITION_NEW_LINE_TABLE = 2
DN_POSITION_NEW_LINE_TABLE = 3


# run a command in cmd
def run_command(command: str) -> int:
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
    print("Press enter to continue ... ", end="", flush=True)

    while True:
        char = getwch()

        if repr(char) == repr("\r"):
            break


# the function for show a splitter line
def splitter_line() -> None:
    "show a splitter line"

    print("-" * 80)


# show a splitter line for table. the arg is position of line that can manage by the const in this module
def splitter_line_table(new_line_position: int, length: int) -> None:
    "show a splitter line for table. the arg is position of line that can manage by the const in this module"

    if new_line_position == 1:
        print("\n" + "-" * length)

    elif new_line_position == 2:
        print("-" * length)

    else:
        print("-" * length + "\n")


# make table for many datas
def table(rows: list, columns: list, show_id: bool = False) -> None:
    "make table for many datas. rows have to be 2D list."

    # valriables
    len_line = len(columns) * 15 + 20

    # start making table
    splitter_line_table(new_line_position=UP_POSITION_NEW_LINE_TABLE, length=len_line)
    print(f"{'#':<5} | ", end="")

    # header
    for column in columns:
        print(f"{column:<15}", end=" | ")
    print()

    splitter_line_table(new_line_position=MID_POSITION_NEW_LINE_TABLE, length=len_line)

    # data
    row_number = 1
    for row in rows:

        if show_id:
            row = list(row)
        else:
            row = list(row)[1:]

        print(f"{row_number:<5}", end=" | ")

        for data in row:
            print(f"{data:<15}", end=" | ")
        print()

        row_number += 1

    splitter_line_table(new_line_position=DN_POSITION_NEW_LINE_TABLE, length=len_line)


# check the number is number and check for the range
def check_number_greater_zero(number: int, greater_that_zero: bool) -> bool:
    "check the number is number and check for the range"

    try:
        number = int(number)

        if greater_that_zero and number > 0:
            return True
        elif not greater_that_zero and number < 0:
            return True

        return False
    except:
        return False
