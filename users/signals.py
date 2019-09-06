# from allauth.account.signals import user_signed_up
#
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
# from .models import CustomUser
# from .models import Profile


# @receiver(signal=post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

# @receiver(user_signed_up)
# def user_signed_up_(request, user, sociallogin=None, **kwargs):
#     """
#     When a social account is created successfully and this signal is received,
#     django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:
#
#     sociallogin.account.provider  # e.g. 'twitter'
#     sociallogin.account.get_avatar_url()
#     sociallogin.account.get_profile_url()
#     sociallogin.account.extra_data['screen_name']
#
#     See the socialaccount_socialaccount table for more in the 'extra_data' field.
#     """
#
#     if sociallogin:
#         # Extract first / last names from social nets and store on User record
#         if sociallogin.account.provider == 'github':
#             name = sociallogin.account.extra_data['name']
#             user.first_name = name.split()[0]
#             user.last_name = name.split()[1]
#             print(f"first_name: {user.first_name}, last_name: {user.last_name}")
#
#         user.save()