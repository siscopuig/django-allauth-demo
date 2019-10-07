from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['email']


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class CustomUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number']


