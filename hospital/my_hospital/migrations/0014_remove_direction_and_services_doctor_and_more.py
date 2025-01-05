# Generated by Django 5.1.4 on 2025-01-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hospital', '0013_direction_and_services_doctor'),
        ('profile_app', '0003_alter_doctorprofile_working_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction_and_services',
            name='doctor',
        ),
        migrations.AddField(
            model_name='direction_and_services',
            name='doctor',
            field=models.ManyToManyField(to='profile_app.doctorprofile'),
        ),
    ]
