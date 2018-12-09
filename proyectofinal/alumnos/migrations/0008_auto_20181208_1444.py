# Generated by Django 2.1.3 on 2018-12-08 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_auto_20181207_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='insc_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de inscripcion'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='exam_date',
            field=models.DateField(verbose_name='Fecha de examen'),
        ),
    ]
