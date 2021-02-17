from django.db import models
from datetime import date

# Create your models here.



class Student(models.Model):
    number_group = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.CharField(choices=number_group, max_length=20)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(max_length=10, blank=True, null=True)
    birthday = models.DateField(default=date.today())
    image = models.ImageField(default='image_student.jpg')
