# Generated by Django 3.1.6 on 2021-02-24 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0026_auto_20210224_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson_school',
            name='points',
        ),
    ]
