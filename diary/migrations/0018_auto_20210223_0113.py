# Generated by Django 3.1.6 on 2021-02-22 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0017_auto_20210220_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_school',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=30)),
                ('image_lesson', models.ImageField(upload_to='')),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile_parent',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2021, 2, 23)),
        ),
        migrations.AlterField(
            model_name='profile_student',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2021, 2, 23)),
        ),
        migrations.AlterField(
            model_name='profile_teacher',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2021, 2, 23)),
        ),
    ]
