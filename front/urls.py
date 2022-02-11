from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student-list', views.studentList, name='student-list'),
    path('student-create', views.studentCreate, name='student-create'),
    path('student-update/<int:id>', views.studentUpdate, name='student-update'),
    path('student-delete/<int:id>', views.studentDelete, name='student-delete'),
]