# Generated by Django 2.1.3 on 2018-12-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0012_auto_20181208_1512'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notas',
            new_name='Nota',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='alumnos', verbose_name='Imagen'),
        ),
    ]
