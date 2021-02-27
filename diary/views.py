from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, PointForm
from .models import Profile_student, Profile_teacher, Lesson_school


# Create your views here.
def magazine_school(request, id_lesson):
    total = 0
    magazine = Lesson_school.objects.get(id=id_lesson)
    points = magazine.points_school_set.all()
    for i in points:
        total += i.points
    form = PointForm(initial={'magazine': magazine, 'user': request.user})
    if request.method == 'POST':
        form = PointForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'diary/school_magazine.html',
                  {'magazine': magazine, 'form': form, 'points': points, 'total': round(total / len(points), 1)})


def lesson(request):
    lessons = Lesson_school.objects.all()
    return render(request, 'diary/lesson.html', {'lessons': lessons})


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
                Profile_student.objects.create(user=request.user, )
            else:
                Profile_teacher.objects.create(first_name='sdfdsf', user=request.user)
            register.save()
            return redirect('lessons')
    return render(request, 'diary/register.html', {'register': register})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('lessons')
    return render(request, 'diary/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')
