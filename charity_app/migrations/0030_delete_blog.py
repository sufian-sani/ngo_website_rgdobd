# Generated by Django 3.2 on 2022-07-25 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0029_alter_blog_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]