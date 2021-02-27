from django.contrib.auth.models import User
from django.db import models
from datetime import date


# Create your models here.


class Profile_student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)


class Profile_teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    birthday = models.DateField(date.today(), blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Lesson_school(models.Model):
    name_lesson = models.CharField(max_length=30)

class Points_school(models.Model):
    lesson = models.ForeignKey(Lesson_school, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile_student,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

