from django.db import models

class CountryChoices(models.TextChoices):
    Cuba = 'Cuba'
    USA = 'USA'
    ## other countries

class ProvinceChoices(models.TextChoices):
    Habana = 'La Habana'
    Artemisa = 'Artemisa'
    ## other provinces

class MunicipalityChoices(models.TextChoices):
    Plaza = 'Plaza de la revolución'
    Playa = 'Playa'
    ## other municipalities

class StateChoices(models.TextChoices):
    Active = 'Active'
    Inactive = 'Inactive'

class SituationChoices(models.TextChoices):
    NewIncome = 'New income'
    Continuing = 'Continuing'
    Repeating = 'Repeating'
    Transfer = 'Transfer'
    ReEntry = 'Re-entry'

class CareerChoices(models.TextChoices):
    ComputerScience = 'Computer Science'
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
    EnabledMediumSuperior = 'Enabled Medium Superior'
    Decree91 = 'Decree 91'
    Order18 = 'Order 18'
    NationalContests = 'National Contests'
    Minint = 'MININT'
    HighPerformanceAthletes = 'High Performance Athletes'
    LevelingCourses = 'Leveling Courses'
    Foreign = 'Foreign'

class AcademicOriginChoices(models.TextChoices):
    PreUniversitary = 'Pre-universitary'
    Foreign = 'Foreign'
    TechnicalAndProfessionalLearning = 'Technical and Professional Learning'
    Order18 = 'Order 18'

class StudyRegimenChoices(models.TextChoices):
    OnlyStudy = 'Only Study'
    StudyAndWork = 'Study and Work'

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
    HalfIntern = 'Half-Intern'
    NationalScolarship = 'National Scolarship'
    InternationalScolarship = 'International Scolarship'

class AcademicLevelChoices(models.TextChoices):
    Basic = 'Basic'
    Medium = 'Medium'
    MediumSuperior = 'Medium Superior'
    Superior = 'Superior'