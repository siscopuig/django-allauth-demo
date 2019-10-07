from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Creates a CustomUser object by keeping the properties of the AbstractUser.
    - Removes username field.
    - Field email become required & unique.
    - Sets USERNAME_FIELD to unique identifier for the User model
    """
    
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    def __str__(self):
        """A string representation of the model."""
        return self.email


class UserProfile(models.Model):
    """ User profile model """
    
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='images/default/default.jpg', null=True)


    def save(self, **kwargs):
        super().save()


    def __str__(self):
        """A string representation of the model."""
        return f"{self.user.email} Profile"

