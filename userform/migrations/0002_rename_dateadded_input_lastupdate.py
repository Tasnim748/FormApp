# Generated by Django 4.1.5 on 2023-01-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='dateAdded',
            new_name='lastUpdate',
        ),
    ]