from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django import forms

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *agrs, **kwargs):
        super(CustomUserLoginForm, self).__init__(*agrs, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"text",
        "placeholder":"Usernamemigizni kiriting"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"password",
        "placeholder":"Parolingizni kiriting"
    }))
class CustomUserCreationForm(UserCreationForm):
#     # username = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"text",
#     #     "placeholder":"Usernamemigizni kiriting"
#     # }))
#     # first_name = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"text",
#     #     "placeholder":"Ismingizni kiriting"
#     # }))
#     # last_name = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"text",
#     #     "placeholder":"Familiyangiz kiriting"
#     # }))
#     # email = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"text",
#     #     "placeholder":"Email pochtangizni kiriting"
#     # }))
#     # age = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"number",
#     #     "placeholder":"Yoshingizni kiriting"
#     # }))
#     # password1 = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"password",
#     #     "placeholder":"Parolingizni kiriting"
#     # }))
#     # password2 = forms.CharField(widget=forms.TextInput(attrs={
#     #     "class":"w3-input w3-border",
#     #     "type":"password",
#     #     "placeholder":"Parolingizni takroran kiriting"
#     # }))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'password1', 'password2',)
#
class CustomUsersChangingForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"text",
        "placeholder":"Ismingizni kiriting"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"text",
        "placeholder":"Familiyangiz kiriting"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"text",
        "placeholder":"Email pochtangizni kiriting"
    }))
    age = forms.CharField(widget=forms.TextInput(attrs={
        "class":"w3-input w3-border",
        "type":"number",
        "placeholder":"Yoshingizni kiriting"
    }))
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'age',)

# class UserRegistrationForm(UserCreationForm):

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border w3-white', 'label': 'Eski parol', 'type': 'password', 'placeholder': "   Oldingi kalit so'zingizni kiriting" }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border w3-white', 'label': 'Yangi parol', 'type': 'password', 'placeholder': "  Yangi kalit so'zni kiriting"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border w3-white','label': 'Yangi parolni takrorlash', 'type': 'password', 'placeholder': "  Yangi kalit so'zni yana bir marta kiriting"}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
