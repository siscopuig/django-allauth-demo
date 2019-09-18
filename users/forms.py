from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class CustomUserProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['address', 'phone_number']


