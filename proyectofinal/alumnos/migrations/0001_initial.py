# Generated by Django 2.1.4 on 2018-12-17 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('insc_date', models.DateField(blank=True, null=True, verbose_name='Fecha de inscripcion')),
                ('dni', models.CharField(default='', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(verbose_name='Fecha de examen')),
                ('calificacion', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Materia')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
            },
        ),
        migrations.AddField(
            model_name='materia',
            name='alumnos',
            field=models.ManyToManyField(through='alumnos.Nota', to='alumnos.Alumno'),
        ),
    ]
