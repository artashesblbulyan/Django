# Generated by Django 4.1.1 on 2022-10-27 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_drive_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drive',
            name='completed',
        ),
    ]
