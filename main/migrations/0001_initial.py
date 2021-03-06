# Generated by Django 3.0.8 on 2021-02-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=10056)),
                ('github_link', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=10056)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
    ]
