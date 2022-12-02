# Generated by Django 3.2 on 2022-07-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url_field', models.URLField(blank=True, null=True)),
                ('subtitle', models.CharField(max_length=500)),
                ('background_image', models.ImageField(upload_to='slider_image')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
