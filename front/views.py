from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .utils import *
from .services import *
import json

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
        print("There was an exception deleting the student: " + str(e))

    return redirect('student-list')

def optimize(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        cant_groups =data['cant_groups']
        id_students =data['id_students']
        prop = data['property']
        students = []
        for idS in id_students:
            students.append(Student.objects.get(id=idS))
        print(prop)
        try:
            result = group_students(students, int(cant_groups), prop, False)
        except:
            result = group_students(students, int(cant_groups), prop, True)
        print(str(result))
        print(age_avg(result))
        return redirect('student-list')


"""Upload Files"""
def upload_file(request):
    excel_file = request.FILES["excel_file"]
    matrix = import_excel_file(excel_file)
    studentsToCreate = get_students_from_excel(matrix)
    for s in studentsToCreate:
        s.save()

    return redirect('student-list')


"""Groups"""
def group_list(request):
    groups = GroupModel.objects.all()
    groups_view = []
    for g in groups:
        groups_view.append({'group': g, 'countStudents': len(g.students.all())})

    return render(request, 'group-list.html', {'groups': groups_view})


def create_group(request):
    if request.method == "POST":  
        group_name = request.POST['name']
        if group_name != '':
            try:  
                new_group = GroupModel(name = group_name)
                new_group.save()
                return redirect('group-list')
            except Exception as e:
                print("There was an exception creating the group: " + e)

    return render(request, 'create-group.html')


def delete_group(request, id):
    group = GroupModel.objects.get(id=id)
    try:
        group.delete()
    except Exception as e:
        print("There was an exception deleting the group: " + e)

    return redirect('group-list')


def group_students_view(request, id):
    group = GroupModel.objects.get(id=id)
    all_students = Student.objects.all()
    group_students = group.students.all()
    
    students_in, students_out = get_students_group(group_students, all_students)

    return render(request, 'group-students.html',
                  {'group': group, 'studentsIn': students_in, 'studentsOut': students_out})


def add_student_to_group(request, id_group, id_student):
    group = GroupModel.objects.get(id=id_group)
    student = Student.objects.get(id=id_student)
    group.students.add(student)

    return redirect('group-students', id=group.id)


def remove_student_to_group(request, id_group, id_student):
    group = GroupModel.objects.get(id=id_group)
    student = Student.objects.get(id=id_student)
    group.students.remove(student)

    return redirect('group-students', id=group.id)


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
