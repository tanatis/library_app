# Generated by Django 4.2.3 on 2023-07-15 17:13

import django.core.validators
from django.db import migrations, models
import library_app.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_email_alter_appuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3), library_app.core.validators.username_validator]),
        ),
    ]
