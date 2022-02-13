import openpyxl
from .models import Student

def import_excel_file(file):
    # TODO (OPTIONAL): put validations

    wb = openpyxl.load_workbook(file)

    # getting a particular sheet by name out of many sheets
    worksheet = wb["Estudiantes1"]

    excel_data = list()
    # iterating over the rows and
    # getting value from each cell in row
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)

    return excel_data

def get_students_from_excel(matrix):
    result = []
    for i in range(1,len(matrix)):
        s = matrix[i]
        student = Student(
            identity_Number = s[0],
            name= s[1],
            last_Name = s[2],
            country = s[3],
            province = s[4],
            municipality = s[5],
            situation = s[6],
            state = s[7],
            address = s[8],
            birth_Date = s[9],
            career = s[11],
            faculty = s[12],
            course_Type = s[13],
            mail = s[14],
            source_of_Income = s[15],
            academic_Origin = s[16],
            study_Regimen = s[17],
            natural_From = s[18],
            phone_Number = s[19],
            es_Income_Date = s[20],
            civil_State = s[21],
            political_Organization = s[22],
            ces_Income_Date = s[23],
            enrollment_Date = s[24],
            sex = s[25],
            skin_Color = s[26],
            student_Type = s[27],
            study_Year = s[28],
            work_Center = s[29],
            fathers_Name = s[30],
            fathers_Academic_Level = s[31],
            mothers_Name = s[32],
            mothers_Academic_Level = s[33],
            military_Service_Type = s[34],
            age = s[35]
        )
        result.append(student)
    return result