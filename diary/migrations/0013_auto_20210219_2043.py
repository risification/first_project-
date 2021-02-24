# Generated by Django 3.1.6 on 2021-02-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0012_auto_20210219_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_parent',
            name='group',
        ),
        migrations.RemoveField(
            model_name='profile_teacher',
            name='group',
        ),
        migrations.AddField(
            model_name='profile_teacher',
            name='lesson',
            field=models.CharField(choices=[('english', 'english'), ('algebra', 'algebra'), ('art', 'art')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]