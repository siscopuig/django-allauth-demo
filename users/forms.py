from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import UserProfile


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


