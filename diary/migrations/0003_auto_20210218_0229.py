# Generated by Django 3.1.6 on 2021-02-17 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('lesson', models.CharField(choices=[('algebra', 'algebra'), ('geography', 'geography'), ('Informatics', 'Informatics')], max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.date(2021, 2, 18)),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='media/image_student.jpg', upload_to=''),
        ),
    ]
