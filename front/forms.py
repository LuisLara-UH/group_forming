import datetime

from django.forms import ModelForm, DateInput
from .models import Student
import django.forms as forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birth_Date': forms.SelectDateWidget(),
            'enrollment_Date': forms.SelectDateWidget(),
            'es_Income_Date': forms.SelectDateWidget(),
            'ces_Income_Date': forms.SelectDateWidget(),
        }
