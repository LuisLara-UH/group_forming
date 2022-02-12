import openpyxl

def import_excel_file(file):
    # TODO put validation here to check excel extension

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

    # TODO save the data into the database