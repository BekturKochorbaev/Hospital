# Generated by Django 5.1.4 on 2025-01-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hospital', '0010_procedurename_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction_and_services',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]