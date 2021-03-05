from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from diary.models import Points_school


class SignupForm(UserCreationForm):
    type_user = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'type_user', 'password1', 'password2')


class PointForm(forms.ModelForm):
    class Meta:
        model = Points_school
        fields = '__all__'
