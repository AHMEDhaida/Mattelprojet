# Generated by Django 3.0.7 on 2020-09-12 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='lieu',
            new_name='nameD',
        ),
        migrations.RemoveField(
            model_name='direction',
            name='ville',
        ),
    ]
