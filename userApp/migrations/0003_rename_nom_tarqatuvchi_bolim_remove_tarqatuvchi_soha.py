# Generated by Django 5.0.2 on 2024-03-03 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_tarqatuvchi_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarqatuvchi',
            old_name='nom',
            new_name='bolim',
        ),
        migrations.RemoveField(
            model_name='tarqatuvchi',
            name='soha',
        ),
    ]
