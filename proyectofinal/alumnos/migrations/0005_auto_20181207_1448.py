# Generated by Django 2.1.3 on 2018-12-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_auto_20181207_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='exam_date',
            field=models.DateField(),
        ),
    ]
