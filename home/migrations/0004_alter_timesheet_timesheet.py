# Generated by Django 5.0.2 on 2024-02-19 13:34

import django.core.validators
import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='timesheet',
            field=models.FileField(upload_to=home.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['xls', 'xlsx'])]),
        ),
    ]
