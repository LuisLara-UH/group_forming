from django.db import models

import front.models
from .model_choices import *


class Student(models.Model):
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

    def __str__(self):
        try:
            return self.name + " " + self.last_Name
        except:
            return 'Sin Nombre'

    identity_Number = models.CharField(db_column='identity_number', max_length=100, blank=False)
    name = models.CharField(db_column='name', max_length=100, blank=False)
    last_Name = models.CharField(db_column='last_name', max_length=100, blank=False)
    country = models.CharField(max_length=100, choices=CountryChoices.choices, default=CountryChoices.Cuba)
    province = models.CharField(max_length=100, choices=ProvinceChoices.choices, default=ProvinceChoices.Habana)
    municipality = models.CharField(max_length=100, choices=MunicipalityChoices.choices,
                                    default=MunicipalityChoices.Playa)
    situation = models.CharField(max_length=100, choices=SituationChoices.choices, default=StateChoices.Active)
    state = models.CharField(max_length=100, choices=StateChoices.choices, default=SituationChoices.New_Income)
    address = models.CharField(db_column='address', max_length=100, blank=False)
    birth_Date = models.DateField(db_column='birth_date', max_length=100, blank=False)
    career = models.CharField(max_length=100, choices=CareerChoices.choices, default=CareerChoices.Computer_Science)
    faculty = models.CharField(max_length=100, choices=FacultyChoices.choices, default=FacultyChoices.Matcom)
    course_Type = models.CharField(max_length=100, choices=CourseTypeChoices.choices,
                                   default=CourseTypeChoices.Daily)
    mail = models.EmailField(db_column='mail', max_length=100, blank=False)
    source_of_Income = models.CharField(max_length=100, choices=SourceOfIncomeChoices.choices,
                                        default=SourceOfIncomeChoices.PreUniversitary)
    academic_Origin = models.CharField(max_length=100, choices=AcademicOriginChoices.choices,
                                       default=AcademicOriginChoices.PreUniversitary)
    study_Regimen = models.CharField(max_length=100, choices=StudyRegimenChoices.choices,
                                     default=StudyRegimenChoices.Only_Study)
    natural_From = models.CharField(db_column='natural_from', max_length=100, blank=False)
    phone_Number = models.CharField(db_column='phone_number', max_length=100, blank=False)
    es_Income_Date = models.DateField(db_column='es_income_date', max_length=100, blank=False)
    civil_State = models.CharField(max_length=100, choices=CivilStateChoices.choices, default=CivilStateChoices.Single)
    political_Organization = models.CharField(db_column='political_organization', max_length=100, blank=False)
    ces_Income_Date = models.DateField(db_column='ces_income_date', max_length=100, blank=False)
    enrollment_Date = models.DateField(db_column='enrollment_date', max_length=100, blank=False)
    sex = models.CharField(db_column='sex', max_length=100, blank=False)
    skin_Color = models.CharField(max_length=100, choices=SkinColorChoices.choices, default=SkinColorChoices.White)
    student_Type = models.CharField(max_length=100, choices=StudentTypeChoices.choices,
                                    default=StudentTypeChoices.Extern)
    study_Year = models.CharField(db_column='study_year', max_length=100, blank=False)
    work_Center = models.CharField(db_column='work_center', max_length=100, blank=False)
    fathers_Name = models.CharField(db_column='fathers_name', max_length=100, blank=False)
    fathers_Academic_Level = models.CharField(max_length=100, choices=AcademicLevelChoices.choices,
                                              default=AcademicLevelChoices.Superior)
    mothers_Name = models.CharField(db_column='mothers_name', max_length=100, blank=False)
    mothers_Academic_Level = models.CharField(max_length=100, choices=AcademicLevelChoices.choices,
                                              default=AcademicLevelChoices.Superior)
    military_Service_Type = models.CharField(db_column='military_service_type', max_length=100)
    age = models.PositiveIntegerField(db_column='age', blank=False)

    # Relational fields
    # group = models.ForeignKey(front.GroupModel, db_column='group')


class GroupModel(models.Model):
    name = models.CharField(max_length=50)

    # relational fields
    students = models.ManyToManyField(Student, db_column='group_students')
