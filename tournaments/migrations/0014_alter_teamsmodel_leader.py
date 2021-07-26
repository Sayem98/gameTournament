# Generated by Django 3.2.5 on 2021-07-26 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_site', '0008_alter_usermodel_user_image'),
        ('tournaments', '0013_alter_teamsmodel_leader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamsmodel',
            name='leader',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='login_site.usermodel'),
        ),
    ]