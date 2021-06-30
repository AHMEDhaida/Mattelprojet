from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username','first_name', 'last_name', 'email', 'groups', 'is_superuser', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserRole(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups', 'is_superuser']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'image']