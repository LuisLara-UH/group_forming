from .models import Student
from .forms import StudentForm


def get_student_form(student: Student):
    return StudentForm(initial={
        'name': student.name,
        'last_Name': student.last_Name,
        'identity_Number': student.identity_Number,
        'age': student.age,
        'country': student.country,
        'municipality': student.municipality,
        'situation': student.situation,
        'state': student.state,
        'address': student.address,
        'birth_Date': student.birth_Date,
        'group': student.group,
        'career': student.career,
        'faculty': student.faculty,
        'course_Type': student.course_Type,
        'mail': student.mail,
        'source_of_Income': student.source_of_Income,
        'academic_Origin': student.academic_Origin,
        'study_Regimen': student.study_Regimen,
        'natural_From': student.natural_From,
        'phone_Number': student.phone_Number,
        'es_Income_Date': student.es_Income_Date,
        'civil_State': student.civil_State,
        'political_Organization': student.political_Organization,
        'ces_Income_Date': student.ces_Income_Date,
        'enrollment_Date': student.enrollment_Date,
        'sex': student.sex,
        'skin_Color': student.skin_Color,
        'student_Type': student.student_Type,
        'study_Year': student.study_Year,
        'work_Center': student.work_Center,
        'fathers_Name': student.fathers_Name,
        'fathers_Academic_Level': student.fathers_Academic_Level,
        'mothers_Name': student.mothers_Name,
        'mothers_Academic_Level': student.mothers_Academic_Level,
        'military_Service_Type': student.military_Service_Type,
        'age': student.age,
    })


# TODO: fill filter
def filter_students(student_list, property: str):
    pass


# TODO: fill grouping
def group_students(student_list, property: str):
    pass

def get_students_group(groupStudents, all_students):
    studentsIn = []
    studentsOut = []

    for s in all_students:
        if s in groupStudents:
            studentsIn.append(s)
        else:
            studentsOut.append(s)

    return (studentsIn, studentsOut)