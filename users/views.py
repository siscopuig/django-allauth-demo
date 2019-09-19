from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import CustomUserChangeForm
from .forms import CustomUserProfile
from .models import UserProfile


@login_required()
def profile(request):

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

    context = {
        'update_form': update_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context=context)



@login_required()
def delete_user(request):

    if not request.user.is_superuser:
        request.user.delete()
        messages.warning(request, 'Account deleted!')
        return redirect('delete')

    else:
        messages.warning(request, 'Sorry, admin accounts cannot be deleted!.')
        return render(request, 'home.html')

