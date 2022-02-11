# Generated by Django 4.0.2 on 2022-02-10 04:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_student_identity_number_alter_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='study_year',
            new_name='año_de_Estudio',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='career',
            new_name='carrera',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='work_center',
            new_name='centro_de_Trabajo',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='skin_color',
            new_name='color_de_Piel',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mail',
            new_name='correo_Electronico',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='state',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='civil_state',
            new_name='estado_Civil',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='faculty',
            new_name='facultad',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ces_income_date',
            new_name='fecha_de_Ingreso_a_la_CES',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='es_income_date',
            new_name='fecha_de_Ingreso_a_la_ES',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='enrollment_date',
            new_name='fecha_de_Matricula',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='birth_date',
            new_name='fecha_de_Nacimiento',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='source_of_income',
            new_name='fuente_de_Ingreso',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='group',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='municipality',
            new_name='municipio',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='natural_from',
            new_name='natural_de',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mothers_academic_level',
            new_name='nivel_Academico_de_la_Madre',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fathers_academic_level',
            new_name='nivel_Academico_del_Padre',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mothers_name',
            new_name='nombre_de_la_madre',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='fathers_name',
            new_name='nombre_del_Padre',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='phone_number',
            new_name='numero_Telefonico',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='political_organization',
            new_name='organizacion_Politica',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='academic_origin',
            new_name='origen_Academico',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='country',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='province',
            new_name='provincia',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='study_regimen',
            new_name='regimen_de_Estudio',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sex',
            new_name='sexo',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='situation',
            new_name='situacion',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course_type',
            new_name='tipo_de_Curso',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_type',
            new_name='tipo_de_Estudiante',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='military_service_type',
            new_name='tipo_de_Servicio_Militar',
        ),
        migrations.RemoveField(
            model_name='student',
            name='identity_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='CI',
            field=models.CharField(db_column='identity_number', default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='nombre',
            field=models.CharField(db_column='name', default='', max_length=100),
            preserve_default=False,
        ),
    ]