from Database import Database

database_start = Database("database.sqlite3")

# create table of students 
def create_student_table() -> None:
    global database_start

    query = """
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        code VARCHAR(50) NOT NULL UNIQUE
    );
    """

    database_start.Get_Query(query, auto_commit=False)

def create_subjects_table() -> None:
    global database_start

    query = """
    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(50) NOT NULL,
        code VARCHAR(25) NOT NULL UNIQUE,
        unit INTEGER NOT NULL check(unit > 0)
    );
    """

    database_start.Get_Query(query, auto_commit=False)

def create_grades_table() -> None:
    global database_start

    query = """
    CREATE TABLE grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade READ NOT NULL check(grade >= 0 AND grade <= 20),
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """

    database_start.Get_Query(query, auto_commit=False)

def main():
    create_student_table(); create_subjects_table(); create_grades_table()

    database_start.Perform_Queries()

    database_start.Close_database()

if __name__ == "__main__":
    main()
