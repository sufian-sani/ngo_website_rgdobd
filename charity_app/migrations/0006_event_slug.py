# Generated by Django 3.2 on 2022-07-21 10:09

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0005_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]