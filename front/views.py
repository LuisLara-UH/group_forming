from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .utils import import_excel_file

def home(request):
    # TODO: Fill this view with the initial page
    return render(request, 'home.html', {'name': 'World'})

def studentList(request):  
    students = Student.objects.all()  
    return render(request,"student-list.html",{'students':students})  

def studentCreate(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('student-list')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'student-create.html',{'form':form})  

def studentUpdate(request, id):  
    student = Student.objects.get(id=id)
    form = StudentForm(initial={
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
    if request.method == "POST":  
        form = StudentForm(request.POST, instance=student)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('student-list')  
            except Exception as e: 
                pass    
    return render(request,'student-update.html',{'form':form})  

def studentDelete(request, id):
    student = Student.objects.get(id=id)
    try:
        student.delete()
    except:
        pass
    return redirect('student-list')

def upload_file(request):
    excel_file = request.FILES["excel_file"]
    import_excel_file(excel_file)

    return redirect('student-list') 