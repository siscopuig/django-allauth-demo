from django import forms
from users.models import Profile
from allauth.account.forms import SignupForm


class CustomSignupForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address', 'phone_number']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.address = self.cleaned_data['address']
        user.profile.phone_number = self.cleaned_data['phone_number']
        user.profile.save()


address = forms.CharField(max_length=30, label='Address')
phone_number = forms.CharField(max_length=30, label='Phone Number')

# On settings.py
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}
# ACCOUNT_SIGNUP_FORM_CLASS = 'UsersConfig.forms.CustomSignupForm'