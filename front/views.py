from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .utils import import_excel_file
from .services import *


def home(request):
    # TODO: Fill this view with the initial page
    return render(request, 'home.html', {'name': 'World'})


def student_list(request):
    students = Student.objects.all()  
    return render(request, "student-list.html", {'students': students})


def student_create(request):
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
    return render(request, 'student-create.html', {'form': form})


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = get_student_form(student)
    if request.method == "POST":  
        form = StudentForm(request.POST, instance=student)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('student-list')  
            except Exception as e: 
                pass    
    return render(request, 'student-update.html', {'form': form})


def student_delete(request, id):
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