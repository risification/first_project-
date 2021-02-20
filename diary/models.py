from django.db import models
from datetime import date


# Create your models here.


class Profile_student(models.Model):
    group_number = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    birthday = models.DateField(date.today(), blank=True, null=True)
    group = models.CharField(choices=group_number, max_length=20)
    email = models.EmailField(blank=True, null=True)


class Profile_teacher(models.Model):
    lesson_type = (
        ('english', 'english'),
        ('algebra', 'algebra'),
        ('art', 'art'),
    )
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    birthday = models.DateField(date.today(), blank=True, null=True)
    lesson = models.CharField(choices=lesson_type, max_length=30)
    email = models.EmailField(blank=True, null=True)


class Profile_parent(models.Model):
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    birthday = models.DateField(date.today(), blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
