# Generated by Django 3.2 on 2022-07-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0004_category_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_image'),
        ),
    ]
