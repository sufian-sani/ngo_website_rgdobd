# Generated by Django 3.2 on 2022-07-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0044_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
