# Generated by Django 4.1 on 2023-11-24 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='owner',
        ),
    ]
