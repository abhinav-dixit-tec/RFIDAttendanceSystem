# Generated by Django 4.2 on 2023-06-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_stud_cardno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='cardno',
            field=models.CharField(max_length=30),
        ),
    ]
