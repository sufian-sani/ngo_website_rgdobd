# Generated by Django 3.2 on 2022-07-25 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0026_auto_20220725_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated',
        ),
    ]