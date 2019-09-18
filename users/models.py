from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='images/default.jpg', null=True)


    def save(self, **kwargs):
        super().save()


    def __str__(self):
        return f"{self.user.username} Profile"

