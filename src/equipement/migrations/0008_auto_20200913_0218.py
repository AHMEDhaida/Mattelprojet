# Generated by Django 3.0.7 on 2020-09-12 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0007_auto_20200913_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='TypeEtat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipement.TypeEtat'),
        ),
    ]
