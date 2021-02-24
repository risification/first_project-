from django.shortcuts import render
from .models import Profile_student, Profile_teacher, Lesson_school


# Create your views here.
def magazine_school(request):
    magazine = Lesson_school.objects.all()
    return render(request, 'diary/school_magazine.html', {'magazine': magazine})


def student_profile_page(request, student_id):
    profile_student = Profile_student.objects.get(id=student_id)
    return render(request, 'diary/profile_student.html', {'student': profile_student})


def teacher_profile_page(request, teacher_id):
    teacher = Profile_teacher.objects.get(id=teacher_id)
    return render(request, 'diary/profile_teacher.html', {'teacher': teacher})


