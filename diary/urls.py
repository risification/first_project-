from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student_page/<int:id_student>/', student_point, name='student'),
    path('teacher_page/', teacher_profile_page, name='teacher'),
    path('school_magazine/<int:id_lesson>/', magazine_school, name='magazine'),
    path('register_school/', register_page, name='register'),
    path('', lesson, name='lessons'),
    path('login_page/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('students/', all_students, name='students'),
    path('views_points/<int:id_student>/', points_views,name='student_points'),
    path('list_lesson_student/',list_lesson,name='list_lesson_student')
]
