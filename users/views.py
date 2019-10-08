from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserProfile


def signup(request):
    """ Signup form view """
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"Account created for {email}.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', context={'form': form})


@login_required()
def profile(request):
    """ Profile view display's  """

    user_profile = UserProfile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = CustomUserProfile(request.POST, instance=user_profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')
    else:
        update_form = CustomUserChangeForm(instance=request.user)
        profile_form = CustomUserProfile(instance=user_profile)
        
    return render(request, 'profile.html', 
                  context={'update_form': update_form, 'profile_form': profile_form})


@login_required()
def delete_user(request):
    """ Deletes user object """

    # Avoids delete an admin user
    if request.user.is_superuser:
        messages.warning(request, 'Sorry, admin accounts cannot be deleted!.')
        return render(request, 'home.html')

    request.user.delete()
    messages.warning(request, 'Account deleted!')
    return redirect('signup')
