# Generated by Django 3.2 on 2022-07-23 09:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0015_partnersnetworks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awardsrecognation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Awards & Recognation',
                'verbose_name_plural': 'Awards & Recognation',
            },
        ),
    ]