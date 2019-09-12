from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    avatar_url = models.CharField(max_length=250, null=True, blank=True)


class Profile(models.Model):

    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def save(self, **kwargs):
        super().save()


    def __str__(self):
        """
        :return:
        """
        return f"{self.user.username} Profile"


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()