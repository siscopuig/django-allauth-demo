from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    pass

class Profile(models.Model):

    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True)


    def save(self, **kwargs):
        super().save()

        # img = Image.open(self.image.path)
        # if img.width > 300 or img.height > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save()


    def __str__(self):
        return f"{self.user.username} Profile"