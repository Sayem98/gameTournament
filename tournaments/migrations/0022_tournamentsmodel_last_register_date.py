# Generated by Django 3.2.5 on 2021-07-27 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0021_alter_tournamentsmodel_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentsmodel',
            name='last_register_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]