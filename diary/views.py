from django.shortcuts import render, redirect

from .forms import SignupForm
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

def register_page(request):
    register = SignupForm()
    if request.method == 'POST':
        register = SignupForm(request.POST)
        if register.is_valid():
            if register.cleaned_data['type_user'] == 'student':
                Profile_student.objects.create(user= request.user,phone= 0,)
            else:
                Profile_teacher.objects.create(first_name='sdfdsf',phone=0,user=request.user)
            register.save()
            return redirect('school_magazine')
    return render(request,'diary/register.html',{'register':register})
