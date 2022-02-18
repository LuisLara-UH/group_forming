from .models import Student, GroupModel
from .forms import StudentForm
from pulp import *
import numpy as np
from datetime import datetime
from gekko import GEKKO
from random import randint


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


def group_students(student_list: [Student], groups_amount: int, field: str, obj_func_null: bool) -> [(Student, GroupModel)]:
    students_amount = len(student_list)

    model = GEKKO(remote=False)
    #model.options.MAX_TIME = 60
    

    # Initialize variables
    decision_vars = [model.Var(lb=0, ub=1, integer=True) for _ in range(students_amount) for _ in range(groups_amount)]
    decision_vars = np.array(decision_vars).reshape((students_amount, groups_amount))
    values = get_values(student_list, field, decision_vars, groups_amount, model)

    print("values", values)
    # Equations
    for i in range(students_amount):
        model.Equation(model.sum([decision_vars[i, j] for j in range(groups_amount)]) == 1)

    for j in range(groups_amount):
        model.Equation(model.sum([decision_vars[i, j] for i in range(students_amount)]) >= int(students_amount / groups_amount))

    for j in range(groups_amount):
        for k in range(groups_amount):
            model.Equation(model.sum([decision_vars[i, j] for i in range(students_amount)]) >=
                           model.sum([decision_vars[i, k] for i in range(students_amount)]) - 1)

    if obj_func_null:
        model.Obj(random_position_value(decision_vars, students_amount, groups_amount) +
                  random_position_value(decision_vars, students_amount, groups_amount) +
                  random_position_value(decision_vars, students_amount, groups_amount))
    else:
        model.Obj(function(student_list, field, decision_vars, groups_amount, model, values))  # Objective

    
    model.solve()
    
    res = [[] for _ in range(groups_amount)]
    for i in range(students_amount):
        for j in range(groups_amount):
            if decision_vars[i, j].value == [1.0]:
                res[j].append(student_list[i])

    
    return res


def get_values(student_list: [Student], field: str, decision_vars, groups_amount: int, model):
    string_number_val = {str: int}
    number_val_count = 500
    result = []
    for student in student_list:
        field_value = student.__dict__[field]
        try:
            string_number_val[field_value]
        except KeyError:
            if field == "age":
                string_number_val[field_value] = int(field_value)
            elif field == "birth_Date" or field == "es_Income_Date" or field == "ces_Income_Date" or field == "enrollment_Date":
                string_number_val[field_value] = datetime.fromtimestamp(field_value)
            else:
                string_number_val[field_value] = number_val_count
                number_val_count += 500

        result.append(string_number_val[field_value])
    return result


def function(student_list: [Student], field: str, decision_vars, groups_amount: int, model, values):
    group_values = [[] for _ in range(groups_amount)]
    for j in range(groups_amount):
        group_values[j] = model.sum([decision_vars[i, j] * values[i]
                                for i in range(len(student_list))])

    return model.sum([distance(group_values[j - 1], group_values[j]) for j in range(1, groups_amount)])


def grouping_value(student_list: [Student], field: str, decision_vars, groups_amount: int, model):
    # Assign values to strings
    string_number_val = {str: int}
    number_val_count = 1
    for student in student_list:
        field_value = student.__dict__[field]
        try:
            string_number_val[field_value]
        except KeyError:
            if field == "age":
                string_number_val[field_value] = int(field_value)
            elif field == "birth_Date" or field == "es_Income_Date" or field == "ces_Income_Date" or field == "enrollment_Date":
                string_number_val[field_value] = datetime.fromtimestamp(field_value)
            else:
                string_number_val[field_value] = number_val_count
                number_val_count += 1

    # Find mean for each group
    group_values = [[] for _ in range(groups_amount)]
    for j in range(groups_amount):
        group_values[j] = model.sum([decision_vars[i, j] * string_number_val[student_list[i].__dict__[field]]
                                for i in range(len(student_list))])

    return model.sum([distance(group_values[j - 1], group_values[j]) for j in range(1, groups_amount)])


def distance(val1: int, val2: int):
    return (val1 - val2)*(val1 - val2)


def random_position_value(items, len1: int, len2: int):
    return items[randint(0, len1), randint(0, len2)]
