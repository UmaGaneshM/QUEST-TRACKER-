# Generated by Django 4.1.7 on 2023-03-02 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0009_alter_createtask_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]