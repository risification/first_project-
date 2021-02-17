from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('student_page/',student_page,name='student')
]