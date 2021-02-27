from django.contrib import admin
from .models import *


# Register your models here.
class Name_lesson(admin.ModelAdmin):
    list_display = ['name_lesson']


admin.site.register([Profile_student, Profile_teacher, Points_school])
admin.site.register(Lesson_school, Name_lesson)
