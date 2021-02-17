from django.shortcuts import render
from .models import Student
# Create your views here.



def student_page(request):
    students = Student.objects.all()
    return render(request,'diary/student.html',{'students':students})