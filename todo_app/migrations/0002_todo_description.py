# Generated by Django 4.0 on 2021-12-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
