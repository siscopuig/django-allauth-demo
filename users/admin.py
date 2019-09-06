from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import CustomUserProfile
from .models import CustomUser
from .models import Profile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)


class UserProfileAdmin(UserAdmin):
    model = Profile
    add_form = CustomUserProfile

admin.site.register(Profile)
