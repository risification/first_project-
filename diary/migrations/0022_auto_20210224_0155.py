# Generated by Django 3.1.6 on 2021-02-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0021_auto_20210224_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_school',
            name='points',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
    ]