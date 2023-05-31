# Generated by Django 4.1.7 on 2023-03-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0006_createtask_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BugName', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=800)),
                ('AraiseDate', models.CharField(max_length=25)),
                ('In_Task', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=20)),
                ('StatusDescription', models.CharField(max_length=256)),
                ('Active', models.BooleanField(default=True)),
                ('file', models.FileField(default=False, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=10)),
                ('EmployeeId', models.CharField(max_length=50)),
                ('Date_Time', models.CharField(max_length=25)),
                ('file', models.FileField(default=False, upload_to='')),
            ],
        ),
    ]