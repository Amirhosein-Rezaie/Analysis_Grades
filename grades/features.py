from database.Database import Database
from grades.tools import search_one_record, TABLE_SBJ, TABLE_STD, check_grade
from subjects.features import search_subject
from tools.func import table

# variables
grade = Database("database.sqlite3")
COLUMNS = ["grade", "student", "subject"]


# # function
# add a grade
def add_grade() -> None:
    "add a grade"

    # variables
    global grade

    student_id = 0
    student_name = ""

    subject_id = 0
    subject_title = ""

    # get ID of the student
    while True:
        student_code = input("Enter the national code of student : ")
        data = search_one_record(student_code, TABLE_STD)

        if data == False:
            print("The student not found ... !")
        else:
            student_id = data[0]
            student_name = data[1] + " " + data[2]
            break

    # get code of the subject
    while True:
        find_sbj_search = search_subject()

        if find_sbj_search == 0:
            break

    # get ID of the subject
    while True:
        subject_code = input("Enter the code of subject : ")

        data = search_one_record(subject_code, TABLE_SBJ)

        if data == False:
            print("The subject not found ... !")
        else:
            subject_id = data[0]
            subject_title = data[1]
            break

    # add the grade for student in the subject
    grade_number = 0.0
    while True:
        grade_number = float(
            input(
                f"Enter the grade for '{student_name}' in '{subject_title}' subject : "
            )
        )

        if check_grade(grade_number):
            break
        else:
            print("Enter grade for student as a number ... !")

    # try add grade
    try:
        grade.Get_Query(
            f"INSERT INTO grades (grade, student_id, subject_id) VALUES({grade_number}, {student_id}, {subject_id})"
        )

        print(
            f"Adding grade for '{student_name}' in '{subject_title}' subject Successfuly Done ... !"
        )
    except:
        print("Adding grade Failed ... !")


# search the grades of a student in a specific subject
def search_grade() -> int:
    "search the grades of a student in a specific subject"

    # variables
    global grade
    ids = {"student": 0, "subject": 0}

    # get student and subject code for search the IDs
    search = input("Enter the student or subject code (exp: code): ")
    # try to search IDs
    try:
        ids["student"] = search_one_record(search, TABLE_STD)[0]
        ids["subject"] = search_one_record(search, TABLE_SBJ)[0]
    except:
        print("Searching for student and subject Fail ... !")
        return 0

    # try to find the grades of the student or specific subject
    try:
        data = grade.Get_Query(
            f"""
            SELECT grades.id, grades.grade,
            students.firstname || ' ' || students.lastname as student_name,
            subjects.title
            FROM grades, students, subjects
            WHERE (grades.student_id={ids['student']} OR grades.subject_id={ids['subject']})
            AND grades.student_id=students.id AND grades.subject_id=subjects.id
            """,
            fetch_result=True,
        )

        table(data, COLUMNS)
        return 1

    except:
        print("Searching for grade Fail ... !")
        return 0
