from django.shortcuts import render
from .models import Profile_student,Profile_teacher,Profile_parent



# Create your views here.

def student_profile_page(request):
    profile_student = Profile_student.objects.all()
    return render(request,'diary/profile_student.html',{'student':profile_student})

def teacher_profile_page(request):
    profile_teachers = Profile_student.objects.all()
    return render(request,'diary/profile_teacher.html',{'teacher':profile_teachers})

def parents_profile_page(request):
    profile_parents = Profile_student.objects.all()
    return render(request,'diary/profile_parent.html',{'parent':profile_parents})