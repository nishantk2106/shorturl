# Generated by Django 3.1 on 2020-08-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorterner', '0002_auto_20200818_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='update',
        ),
    ]
