# Generated by Django 4.2.3 on 2023-07-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed_count',
            field=models.IntegerField(default=0),
        ),
    ]
