from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from allauth.account.forms import SignupForm, UserForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from allauth.account.forms import LoginForm


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






# class CustomSignupForm(forms.ModelForm):
#
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
#
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'address', 'phone_number']
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#
#         user.profile.address = self.cleaned_data['address']
#         user.profile.phone_number = self.cleaned_data['phone_number']
#         user.profile.save()


# address = forms.CharField(max_length=30, label='Address')
# phone_number = forms.CharField(max_length=30, label='Phone Number')