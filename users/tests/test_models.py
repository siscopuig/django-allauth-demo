from django.test import TestCase
from users.models import CustomUser, UserProfile
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):


    def test_create_customuser(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.assertEquals(self.user1.email, 'user1@example.com')


    def test_create_user_profile(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.assertEquals(UserProfile.objects.count(), 1)


    def test_update_user_profile(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        UserProfile.objects.update(user=self.user1, address='Street User1', phone_number='1234567890')
        profile = get_user_model().objects.last().profile
        self.assertEquals(profile.address, 'Street User1')
        self.assertEquals(profile.phone_number, '1234567890')