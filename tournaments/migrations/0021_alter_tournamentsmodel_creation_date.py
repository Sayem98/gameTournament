# Generated by Django 3.2.5 on 2021-07-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0020_alter_tournamentsmodel_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentsmodel',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]