from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

class UserSignupView(CreateView) :
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
    model = User
    form_class = SignupForm

class LoginView(FormView) :
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:welcome')

    def form_valid(self, form) :
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is None :
            form.add_error('username', "User Not Found")
            return self.form_invalid(form)
        else :
            login(self.request, user=user)
        return super().form_valid(form)
    
def logout_view(request) :
    logout(request)
    return HttpResponseRedirect(reverse('home:welcome'))