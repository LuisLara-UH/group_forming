from .models import Student, GroupModel
from .forms import StudentForm
from pulp import *
import numpy as np


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


def get_students_group(group_students, all_students):
    students_in = []
    students_out = []

    for s in all_students:
        if s in group_students:
            students_in.append(s)
        else:
            students_out.append(s)

    return students_in, students_out


def group_students(student_list: [Student], groups_amount: int, field: str) -> [(Student, GroupModel)]:
    students_amount = len(student_list)

    model = LpProblem("Group forming optimization", LpMinimize)

    variable_indices = [str(i) + str(j) for i in range(1, students_amount + 1) for j in range(1, groups_amount + 1)]
    decision_vars = LpVariable.matrix("X", variable_indices, cat="Binary")
    decision_vars = np.array(decision_vars).reshape(students_amount, groups_amount)

    model += grouping_value(student_list, field, decision_vars, groups_amount)
    for i in range(students_amount):
        model += lpSum(decision_vars[i, j] for j in range(groups_amount)) == 1

    for j in range(groups_amount):
        model += lpSum(decision_vars[i, j] for i in range(students_amount)) >= int(students_amount / groups_amount)

    model.solve()

    res = [[] for _ in range(groups_amount)]
    for i in range(students_amount):
        for j in range(groups_amount):
            if decision_vars[i, j].varValue == 1:
                res[j].append(student_list[i])

    return res


def grouping_value(student_list: [Student], field: str, decision_vars, groups_amount: int):
    # Assign values to strings
    string_number_val = {str: int}
    number_val_count = 1
    for student in student_list:
        field_value = student.__dict__[field]
        try:
            string_number_val[field_value]
        except KeyError:
            string_number_val[field_value] = number_val_count
            number_val_count += 1

    # Find mean for each group
    groups_mean = []
    for j in range(groups_amount):
        students_amount = 0
        values_count = 0
        for i in range(len(student_list)):
            if decision_vars[i, j] == 1:
                students_amount += 1
                student_field_value = string_number_val[student_list[i].__dict__[field]]
                values_count += student_field_value

        groups_mean.append(values_count / students_amount)

    groups_mean.sort()

    return groups_mean[-1] - groups_mean[0]
