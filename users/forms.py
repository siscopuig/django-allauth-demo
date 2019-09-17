from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from allauth.socialaccount.forms import DisconnectForm
from django.contrib.auth.forms import User
from django.contrib.auth import get_user_model


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


class CustomSocialDisconnectForm(DisconnectForm):

    def save(self):

        # Add your own processing here if you do need access to the
        # socialaccount being deleted.

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(CustomSocialDisconnectForm, self).save()

        # Add your own processing here if you don't need access to the
        # socialaccount being deleted.


