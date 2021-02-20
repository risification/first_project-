from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('student_page/',student_profile_page,name='student'),
    path('teacher_page/',teacher_profile_page,name='teacher'),
    path('parent_page/',parents_profile_page,name='parent')
]