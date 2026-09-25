from students.features import student
from subjects.features import subject


# # functions
# search for student by national code and return data of one student
def search_student(national_code: str) -> bool | list:
    "search for student by national code and return data of one student"

    data = student.Get_Query(
        f"SELECT * FROM students WHERE code='{national_code}'", fetch_result=True
    )

    if data != []:
        return data[0]
    else:
        return False

