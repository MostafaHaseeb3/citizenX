# Generated by Django 3.1.5 on 2021-07-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RPi', '0002_auto_20210707_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='data',
            new_name='date',
        ),
    ]