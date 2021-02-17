from django.contrib import admin
from .models import *


# Register your models here.
class Srudent_top(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'group', 'address', 'phone_number', 'birthday']


admin.site.register(Student, Srudent_top)
