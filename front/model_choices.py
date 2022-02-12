from django.db import models

# TODO: fill missing values
class CountryChoices(models.TextChoices):
    Cuba = 'Cuba'
    USA = 'USA'
    ## other countries

class ProvinceChoices(models.TextChoices):
    Habana = 'La Habana'
    Artemisa = 'Artemisa'
    ## other provinces

class MunicipalityChoices(models.TextChoices):
    Plaza_de_la_Revolucion = 'Plaza de la revolucion'
    Playa = 'Playa'
    ## other municipalities

class StateChoices(models.TextChoices):
    Active = 'Active'
    Inactive = 'Inactive'

class SituationChoices(models.TextChoices):
    New_Income = 'New income'
    Continuing = 'Continuing'
    Repeating = 'Repeating'
    Transfer = 'Transfer'
    ReEntry = 'Re-entry'

class CareerChoices(models.TextChoices):
    Computer_Science = 'Computer Science'
    Math = 'Math'
    ## other careers

class FacultyChoices(models.TextChoices):
    Matcom = 'Matcom'
    ## other faculties

class CourseTypeChoices(models.TextChoices):
    Daily = 'Daily'
    Nightly = 'Nightly'
    ## other course types

class SourceOfIncomeChoices(models.TextChoices):
    PreUniversitary = 'Pre-universitary'
    Enabled_Medium_Superior = 'Enabled Medium Superior'
    Decree_91 = 'Decree 91'
    Order_18 = 'Order 18'
    National_Contests = 'National Contests'
    Minint = 'MININT'
    High_Performance_Athletes = 'High Performance Athletes'
    Leveling_Courses = 'Leveling Courses'
    Foreign = 'Foreign'

class AcademicOriginChoices(models.TextChoices):
    PreUniversitary = 'Pre-universitary'
    Foreign = 'Foreign'
    Technical_And_Professional_Learning = 'Technical and Professional Learning'
    Order_18 = 'Order 18'

class StudyRegimenChoices(models.TextChoices):
    Only_Study = 'Only Study'
    Study_And_Work = 'Study and Work'

class CivilStateChoices(models.TextChoices):
    Single = 'Single'
    Married = 'Married'
    Divorced = 'Divorced'
    Widower = 'Widower'

class SkinColorChoices(models.TextChoices):
    White = 'White'
    Black = 'Black'
    Brown = 'Brown'

class StudentTypeChoices(models.TextChoices):
    Intern = 'Intern'
    Extern = 'Extern'
    Half_Intern = 'Half-Intern'
    National_Scolarship = 'National Scolarship'
    International_Scolarship = 'International Scolarship'

class AcademicLevelChoices(models.TextChoices):
    Basic = 'Basic'
    Medium = 'Medium'
    Medium_Superior = 'Medium Superior'
    Superior = 'Superior'