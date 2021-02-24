from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('student_page/<int:student_id>/',student_profile_page,name='student'),
    path('teacher_page/<int:teacher_id>/',teacher_profile_page,name='teacher'),
    path('school_magazine',magazine_school,name='magazine'),
    path('register_school',register_page,name = 'register'),
]