# Generated by Django 3.0.7 on 2020-09-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0003_auto_20200915_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='date_update',
            field=models.DateTimeField(null=True),
        ),
    ]
