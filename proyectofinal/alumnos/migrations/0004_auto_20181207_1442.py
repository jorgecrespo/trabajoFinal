# Generated by Django 2.1.3 on 2018-12-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_auto_20181207_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='insc_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]