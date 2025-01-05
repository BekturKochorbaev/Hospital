# Generated by Django 5.1.4 on 2025-01-02 09:19

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_alter_doctorprofile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='working_days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=56),
        ),
    ]
