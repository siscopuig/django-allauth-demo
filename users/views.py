from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .models import Profile
from .forms import CustomUserProfile
from .forms import CustomUserChangeForm
from django.contrib import messages



@login_required()
def profile(request):

    user_model = CustomUser.objects.get(pk=request.user.id)
    user_profile = Profile.objects.get(pk=request.user.id)

    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, instance=user_model)
        profile_form = CustomUserProfile(request.POST, instance=user_profile)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')

    else:
        update_form = CustomUserChangeForm(instance=user_model)
        profile_form = CustomUserProfile(instance=user_profile)

    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context=context)



@login_required()
def delete_user(request):

    user_model = CustomUser.objects.get(pk=request.user.id)

    if not user_model.is_superuser:
        user_model.delete()
        return redirect('delete')
    else:
        messages.warning(request, 'Cannot delete an admin account!!')
        return render(request, 'home.html')




























# @login_required()
# def disconnect(request):
#
#     # user = CustomUser.objects.get(pk=request.user.id)
#
#     form = CustomSocialDisconnectForm()
#     print(form)
#
#     return render(request, 'disconnect.html', context={'form': form})



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


