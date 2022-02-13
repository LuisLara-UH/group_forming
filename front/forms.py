import datetime

from django.forms import ModelForm, DateInput
from .models import Student
import django.forms as forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birth_Date': forms.SelectDateWidget(years=range(1990, 2022)),
            'enrollment_Date': forms.SelectDateWidget(years=range(1990, 2022)),
            'es_Income_Date': forms.SelectDateWidget(years=range(1990, 2022)),
            'ces_Income_Date': forms.SelectDateWidget(years=range(1990, 2022)),
        }
