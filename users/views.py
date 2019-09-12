from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import CustomSignupForm
from .models import CustomUser
from .models import Profile
from .forms import CustomUserProfile
from .forms import CustomUserChangeForm
from django.contrib import messages
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount


@login_required()
def profile(request):

    user_model = CustomUser.objects.get(pk=request.user.id)
    # print(f"User model: {user_model}")
    user_profile = Profile.objects.get(pk=request.user.id)
    # print(f"User profile: {user_profile}")

    data_form = {}

    user = CustomUser.objects.get(pk=request.user.id)

    data_form['first_name'] = user.first_name
    data_form['last_name'] = user.last_name


    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, instance=user_model, initial=data_form)
        profile_form = CustomUserProfile(request.POST, instance=user_profile)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')

    else:
        update_form = CustomUserChangeForm(request.POST, instance=user_model, initial=data_form)
        profile_form = CustomUserProfile(request.POST, instance=user_profile)

    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context=context)


# def signup(request):
#     """
#
#     :param request:
#     :return:
#     """
#
#     form = UserCreateSignUpForm(request.POST)
#
#     if request.method == 'POST':
#         form = UserCreateSignUpForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for username {username}")
#             return redirect('login')
#
#     return render(request, 'signup.html', {"form": form})


