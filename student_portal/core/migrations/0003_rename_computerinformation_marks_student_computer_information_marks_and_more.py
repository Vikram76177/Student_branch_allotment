# Generated by Django 5.0.4 on 2024-04-13 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_student_computerinformation_marks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='computerinformation_marks',
            new_name='computer_information_marks',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='socialscience_marks',
            new_name='social_science_marks',
        ),
    ]
