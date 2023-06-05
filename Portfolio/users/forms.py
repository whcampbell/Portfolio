from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class LoginForm(forms.Form) :
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)