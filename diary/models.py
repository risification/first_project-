from django.db import models
from datetime import date


# Create your models here.


class Profile_student(models.Model):
    gender_type = (
        ('M','M'),
        ('F','F')
    )
    group_number = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    gender = models.CharField(choices=gender_type,max_length=10)
    birthday = models.DateField(date.today(), blank=True, null=True)
    group = models.CharField(choices=group_number, max_length=20)
    email = models.EmailField(blank=True, null=True)


class Profile_teacher(models.Model):
    gender_type = (
        ('M','M'),
        ('F','F')
    )
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=10)
    gender = models.CharField(choices=gender_type,max_length=10)
    birthday = models.DateField(date.today(), blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Lesson_school(models.Model):
    points_type = (
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    name_lesson = models.CharField(max_length=30)
    image_lesson = models.ImageField(default='lesson_image.png')
    points = models.CharField(choices=points_type,max_length=10,blank=True,null=True)
