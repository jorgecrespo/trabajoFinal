# Generated by Django 2.1.3 on 2018-12-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0011_auto_20181208_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='imagen',
        ),
        migrations.AddField(
            model_name='alumno',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]