# Generated by Django 4.2.3 on 2023-08-11 12:23

from django.db import migrations, models
import library_app.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_birth_year_author_death_year_author_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_year',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[library_app.core.validators.author_birth_death_year_validator]),
        ),
    ]