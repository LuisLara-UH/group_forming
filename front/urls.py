from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student-list', views.student_list, name='student-list'),
    path('student-create', views.student_create, name='student-create'),
    path('student-update/<int:id>', views.student_update, name='student-update'),
    path('student-delete/<int:id>', views.student_delete, name='student-delete'),
    path('upload-file', views.upload_file, name='upload-file'),
]