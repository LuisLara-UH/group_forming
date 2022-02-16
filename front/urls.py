from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student-list', views.student_list, name='student-list'),
    path('student-create', views.student_create, name='student-create'),
    path('student-update/<int:id>', views.student_update, name='student-update'),
    path('student-delete/<int:id>', views.student_delete, name='student-delete'),
    path('upload-file', views.upload_file, name='upload-file'),
    path('group-list', views.group_list, name='group-list'),
    path('change-group-name/<int:id>', views.change_group_name, name='change-group-name'),
    path('create-group', views.create_group, name='create-group'),
    path('optimize', views.optimize, name='optimize'),
    path('delete-group/<int:id>', views.delete_group, name='delete-group'),
    path('group-students/<int:id>', views.group_students, name='group-students'),
    path('add-student-to-group/<int:id_group>/<int:id_student>', views.add_student_to_group, name='add-student-to-group'),
    path('remove-student-to-group/<int:id_group>/<int:id_student>', views.remove_student_to_group,
         name='remove-student-to-group'),
]