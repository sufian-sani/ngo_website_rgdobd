# Generated by Django 3.2 on 2022-07-21 11:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0007_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details_optional',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
