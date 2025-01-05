# Generated by Django 5.1.4 on 2025-01-05 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hospital', '0007_alter_name_direction_and_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcedureName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure', models.CharField(max_length=150)),
                ('procedure_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedure_name', to='my_hospital.procedurename')),
            ],
        ),
    ]