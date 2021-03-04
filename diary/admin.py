from django.contrib import admin
from .models import *


# Register your models here.
class Name_lesson(admin.ModelAdmin):
    list_display = ['name_lesson']


class Points_lesson(admin.ModelAdmin):
    list_display = ['lesson', 'student', 'points']


admin.site.register([Profile_student, Profile_teacher])
admin.site.register(Lesson_school, Name_lesson)
admin.site.register(Points_school, Points_lesson)
