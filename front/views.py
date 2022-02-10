from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
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
                return redirect('/front/student-list')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'student-create.html',{'form':form})  

def studentUpdate(request, id):  
    student = Student.objects.get(id=id)
    form = StudentForm(initial={'name': student.name, 'last_name': student.last_Name, 'CI': student.identity_Number, 'age': student.age, 'province': student.province})
    if request.method == "POST":  
        form = StudentForm(request.POST, instance=student)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/front/student-list')  
            except Exception as e: 
                pass    
    return render(request,'student-update.html',{'form':form})  

def studentDelete(request, id):
    student = Student.objects.get(id=id)
    try:
        student.delete()
    except:
        pass
    return redirect('/front/student-list')