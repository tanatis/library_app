# Generated by Django 4.2.3 on 2023-07-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0007_alter_author_death_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]