from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        # Does inherited from AbstractUser
        return f"{self.user.first_name} Profile"




# IntegrityError at /accounts/signup/
# NOT NULL constraint failed: users_profile.user_id