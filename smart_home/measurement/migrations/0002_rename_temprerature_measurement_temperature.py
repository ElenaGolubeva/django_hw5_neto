# Generated by Django 4.2.7 on 2024-03-17 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='temprerature',
            new_name='temperature',
        ),
    ]
