from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import CustomSignupForm
from .models import CustomUser
from .forms import CustomUserProfile
from .forms import CustomUserChangeForm
from django.contrib import messages
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount


@login_required()
def profile(request):

    # if request.method == 'POST':
    #     update_form = CustomUserChangeForm(request.POST, instance=request.user)
    #     print(request.POST)
    #     if update_form.is_valid():
    #         update_form.save()
    #         messages.success(request, f"Your account has been updated")
    #         return redirect('profile')
    # else:
    #     update_form = CustomUserChangeForm(request.POST, instance=request.user)
    #
    # return render(request, 'profile.html', context={"update_form": update_form})

    if request.method == 'POST':
        profile_form = CustomUserProfile(request.POST, instance=request.user.username)
        print(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')
    else:
        profile_form = CustomUserProfile(request.POST, instance=request.user.username)

    return render(request, 'profile.html', context={"update_form": profile_form})

    # if request.method == 'POST':
    #     update_form = CustomUserChangeForm(request.POST)
    #     profile_form = CustomUserProfile(request.POST)
    #     # update_form = CustomUserChangeForm(request.POST, instance=request.user)
    #     # profile_form = CustomUserProfile(request.POST, instance=request.user)
    #
    #     if update_form.is_valid() and profile_form.is_valid():
    #         update_form.save()
    #         profile_form.save()
    #         messages.success(request, f"Your account has been updated")
    #         return redirect('profile')
    #
    # else:
    #     update_form = CustomUserChangeForm(request.POST)
    #     profile_form = CustomUserProfile(request.POST)
    #     # update_form = CustomUserChangeForm(request.POST, instance=request.user)
    #     # profile_form = CustomUserProfile(request.POST, instance=request.user)
    #
    # context = {
    #     'update_form': update_form,
    #     'profile_form': profile_form
    # }
    #
    # return render(request, 'profile.html', context=context)


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


