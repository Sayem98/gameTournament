# Generated by Django 3.2.5 on 2021-07-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0022_tournamentsmodel_last_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentsmodel',
            name='last_register_date',
            field=models.DateField(),
        ),
    ]