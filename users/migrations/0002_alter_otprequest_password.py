# Generated by Django 5.1.6 on 2025-02-25 14:57

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='password',
            field=models.CharField(default=users.models.Generateotp, max_length=4),
        ),
    ]
