# Generated by Django 4.2 on 2023-06-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud',
            name='cardno',
            field=models.CharField(default='N', max_length=30),
        ),
    ]
