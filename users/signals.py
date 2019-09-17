# The callback function which will be connected to this signal.
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from allauth.account.signals import user_logged_in
from django.db.models.signals import post_save
from .models import Profile
from .models import CustomUser
from django.conf import settings
import requests
import shutil


@receiver(signal=post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """
    Does create a user profile for each user when a new user is created.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """

    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    """

    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.profile.save()


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    """
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the
    remote account, e.g.:

    See the socialaccount_socialaccount table for more in the 'extra_data' field.
    """

    # DoesNotExist at /accounts/github/login/callback/
    # Profile matching query does not exist.
    user_profile = Profile.objects.get(pk=request.user.id)

    if sociallogin:
        if sociallogin.account.provider == 'github':
            name = sociallogin.account.extra_data['name']
            first_name = name.split()[0]
            last_name = name.split()[1]
            user_profile.avatar_url = sociallogin.account.extra_data['avatar_url']
            filename = f"social_image/{first_name}_{last_name}_picture.jpg"
            download_social_profile_image(filename, user_profile.avatar_url)
            user_profile.image = filename


    user_profile.save()


# @receiver(user_logged_in)
# def user_looged_in_(request, user, sociallogin=None, **kwargs):
#     """
#     Test logged in signal callback
#     """
#
#     user_profile = Profile.objects.get(pk=request.user.id)
#
#
#     if sociallogin:
#         if sociallogin.account.provider == 'github':
#             name = sociallogin.account.extra_data['name']
#             first_name = name.split()[0]
#             last_name = name.split()[1]
#             user_profile.avatar_url = sociallogin.account.extra_data['avatar_url']
#             filename = f"social_image/{first_name}_{last_name}_picture.jpg"
#             download_social_profile_image(filename, user_profile.avatar_url)
#             user_profile.social_image = filename
#     else:
#         print("Storing default profile image in profile model")
#         user_profile.social_image = 'social_image/default.jpg'
#
#     user_profile.save()



def download_social_profile_image(filename, social_avatar_url):
    """
    Download image from url
    :param filename:
    :param social_avatar_url:
    :return:
    """
    try:

        with open(filename, 'wb') as output_file, \
                requests.get(social_avatar_url, stream=True) as response:
            shutil.copyfileobj(response.raw, output_file)

    except Exception as e:
        print(e)





