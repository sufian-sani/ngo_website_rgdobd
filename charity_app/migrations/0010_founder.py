# Generated by Django 3.2 on 2022-07-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0009_auto_20220721_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=100)),
                ('images', models.FileField(upload_to='founder_image/')),
                ('speech', models.TextField()),
            ],
            options={
                'verbose_name': 'Founder',
                'verbose_name_plural': 'Founder',
            },
        ),
    ]
