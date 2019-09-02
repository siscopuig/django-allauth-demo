from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import CustomSignupForm
from .forms import CustomUserProfile
from .forms import CustomUserChangeForm

from django.contrib import messages


@login_required()
def profile(request):

    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST)
        profile_form = CustomUserProfile(request.POST)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')

    else:
        update_form = CustomUserChangeForm(request.POST)
        profile_form = CustomUserProfile(request.POST)

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


