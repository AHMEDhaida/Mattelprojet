# Generated by Django 3.0.7 on 2020-07-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0003_auto_20200715_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_direction', models.CharField(max_length=25)),
            ],
        ),
    ]
