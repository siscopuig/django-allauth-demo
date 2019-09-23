from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.db.models.signals import post_save
from .models import CustomUser
from .models import UserProfile
from django.conf import settings
import requests
import shutil
import os


@receiver(signal=post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile object when CustomUser object is created.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(signal=post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    """
    Saves user profile.
    """
    instance.profile.save()


@receiver(user_logged_in)
def user_looged_in_(request, user, sociallogin=None, **kwargs):
    """
    When log in with a social account a signal is received, django-allauth passes in the
    sociallogin param, giving access to metadata on social remote account.
    """

    try:
        user_profile = UserProfile.objects.get(pk=request.user.id)
    except UserProfile.DoesNotExist:
        user_profile = None

    if sociallogin:
        if sociallogin.account.provider == 'github':
            username = sociallogin.account.extra_data['login']
            id = sociallogin.account.extra_data['id']
            avatar_url = sociallogin.account.extra_data['avatar_url']
            user_profile.image = f"images/{username}_{id}.jpg"
            process_social_profile_image(user_profile.image, avatar_url)

    user_profile.save()


def process_social_profile_image(filename, avatar_url):
    """
    Download social account avatar.
    """

    dest_path = f'{settings.BASE_DIR}/media/{filename}'

    with open(dest_path, 'wb') as output_file, \
            requests.get(avatar_url, stream=True) as response:
        shutil.copyfileobj(response.raw, output_file)

    if os.path.exists(dest_path):
        print(f"Successfully downloaded social image avatar in: {dest_path}")
    else:
        print("Failed to download social image avatar!")


