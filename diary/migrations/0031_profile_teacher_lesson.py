# Generated by Django 3.1.6 on 2021-03-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0030_auto_20210301_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_teacher',
            name='lesson',
            field=models.CharField(choices=[('art', 'art'), ('algebra', 'algebra'), ('literature', 'literature'), ('Informatics', 'Informatics'), ('physics', 'physics'), ('geography', 'geography')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
