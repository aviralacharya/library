# Generated by Django 5.0.3 on 2024-06-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_student_name_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
