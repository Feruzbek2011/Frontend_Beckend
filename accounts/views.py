from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView
from .models import CustomUser
from django.contrib.auth.models import AbstractUser

from .forms import PasswordChangingForm, CustomUserCreationForm

def SignUpView(request):
    if request.method == "POST":
        username = request.POST['username']
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        age = request.POST['age']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = CustomUser.objects.create_user(username, email, password1)
        myuser.first_name = first
        myuser.last_name = last
        myuser.age = age


        myuser.save()

        return redirect('login')
    return render(request, "registration/signup.html")
def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "home", {'fname':fname})
            print("Noto'g'ri username yoki to'g'ri parol kiritingiz")


        else:
            print("Noto'g'ri username yoki noto'g'ri parol kiritingiz")
            return redirect('home')

    return render(request, "registration/login")
# myuser = CustomUser.objects.create_user(username,  email, age, password1)
# myuser.username = username
# myuser.first_name = first
# myuser.last_name = last
# myuser.email = email
# myuser.age = age
# myuser.password = first

# class SignUpView(CreateView, UserCreationForm):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_done')
    template_name = 'password_change_form.html'

# class UsersChangeView(UpdateView):
#     form_class = CustomUsersChangingForm
#     success_url = reverse_lazy('user_done')
#     template_name = 'registration/edit.html'

def UsersChangeView(request):
    profil = request.user
    form = CustomUsersChangingForm(instance=profil)

    if request.method == "POST":
        form = CustomUsersChangingForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('user_done')
    content = {
        'form':form
    }
    return render(request, 'registration/edit.html', content)

class UserChangeDoneView(TemplateView):
    template_name = 'registration/edit_done.html'

class PasswordChangeDoneView(TemplateView):
    template_name='password_change_done.html'
