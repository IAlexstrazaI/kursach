# Generated by Django 4.0.4 on 2022-05-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doska', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(),
        ),
    ]
