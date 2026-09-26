from students.features import student
from subjects.features import subject

# variables
TABLE_STD = "students"
TABLE_SBJ = "subjects"


# # functions
# search for std or sbj by code and returns data for one of each other
def search_one_record(code: str, table: str) -> bool | list:
    "search for std or sbj by code and returns data for one of each other"

    query = f"SELECT * FROM {table} WHERE code='{code}'"
    data = None

    if table == TABLE_STD:
        data = student.Get_Query(query, fetch_result=True)
    elif table == TABLE_SBJ:
        data = subject.Get_Query(query, fetch_result=True)
    else:
        print("name of tables are Wrong ... !")
        return False

    if data != []:
        return data[0]
    else:
        return False


# check grade. check it is greater and equal 0 and smaller and equal 20.
def check_grade(grade: float) -> bool:
    "check grade. check it is greater and equal 0 and smaller and equal 20."

    return grade >= 0.0 and grade <= 20.0
