# Generated by Django 3.2 on 2022-07-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0038_alter_eventregistation_eventid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistation',
            name='eventid',
            field=models.IntegerField(),
        ),
    ]