# Generated by Django 3.2 on 2022-07-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0035_becomeavolunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='becomeavolunteer',
            name='volunteerid',
            field=models.BigIntegerField(unique=True),
        ),
    ]