# The callback function which will be connected to this signal.
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from .models import Profile
from .models import CustomUser
from django.conf import settings




@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    """
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the
    remote account, e.g.:

    See the socialaccount_socialaccount table for more in the 'extra_data' field.
    """

    if sociallogin:
        # Extract first / last names from social nets and store on CustomUser model
        if sociallogin.account.provider == 'github':
            name = sociallogin.account.extra_data['name']
            user.first_name = name.split()[0]
            user.last_name = name.split()[1]
            user.avatar_url= sociallogin.account.extra_data['avatar_url']

    user.save()


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



# def post_save_receiver(sender, instance, created, **kwargs):
#     pass
#
# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)




