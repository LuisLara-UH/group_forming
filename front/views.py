from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .utils import import_excel_file
from .services import *


def home(request):
    # TODO: Fill this view with the initial page
    return render(request, 'home.html', {'name': 'World'})


"""Student"""
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
            except Exception as e:
                print("There was an exception creating the student: " + e)
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
                print("There was an exception updating the student: " + e)

    return render(request, 'student-update.html', {'form': form})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    try:
        student.delete()
    except Exception as e:
        print("There was an exception deleting the student: " + e)

    return redirect('student-list')


"""Upload Files"""
def upload_file(request):
    excel_file = request.FILES["excel_file"]
    import_excel_file(excel_file)

    return redirect('student-list')


"""Groups"""
def group_list(request):
    groups = GroupModel.objects.all()
    groups_view = []
    for g in groups:
        groups_view.append({'group': g, 'countStudents': len(g.students.all())})

    return render(request, 'group-list.html', {'groups': groups_view})


def change_group_name(request, id):
    group = GroupModel.objects.get(id=id)
    form = {'name': group.name}
    if request.method == "POST":
        new_name = request.POST['name']
        if new_name != '':
            try:
                group.name = new_name
                group.save()
                return redirect('group-list')
            except Exception as e:
                print("There was an exception updating the group: " + e)

    return render(request, 'change-group-name.html', {'form': form})
