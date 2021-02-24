from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    type_user = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ('username','type_user','password1','password2')



