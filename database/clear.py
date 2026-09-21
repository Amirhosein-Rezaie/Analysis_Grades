from Database import Database
from tools.func import run_command

clear_database = Database("database.sqlite3")

def clear_all_data() -> None:
    global clear_database

    clear_database.Get_Query(
        "DELETE FROM students", auto_commit=False
    )
    clear_database.Get_Query(
        "DELETE FROM subjects", auto_commit=False
    )
    clear_database.Get_Query(
        "DELETE FROM grades", auto_commit=False
    )

def main():
    global clear_database

    try:
        clear_all_data()
        clear_database.Perform_Queries()

        run_command(r"cls")
        print("All Tables Cleared ... !")
    except:
        print("Error ... ! ")


if __name__ == "__main__": main()
