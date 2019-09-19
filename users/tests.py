from django.test import TestCase
from .models import CustomUser, Profile
from allauth.socialaccount.models import SocialApp


class ProfileTestCase(TestCase):
    """
    Test CustomUser object creation

    """
    def setUp(self):
        self.user1 = CustomUser.objects.create_user('user1', 'user1@example.com', 'user1password')
        self.pro1 = Profile.objects.update(user=self.pro1, address='Street User1', phone_number='1234567890')

        self.user2 = CustomUser.objects.create_user('user2', 'user2@example.com', 'user2password')
        self.pro2 = Profile.objects.update(user=self.pro2, address='Street User2', phone_number='1234567890')


    def test_profile(self):
        user_profile = Profile.objects.get(user=self.cu1)
        address = user_profile.address
        self.assertEqual('victoria road', address)
        phone_number = user_profile.phone_number
        self.assertEqual('1234567890', phone_number)
        image = user_profile.image
        self.assertEqual('images/default.jpg', image)


    def test_delete_user(self):
        self.client.login(username='user1', password='user1password')
        logged_in_delete_response = self.client.get('/users/delete/')
        self.assertContains(logged_in_delete_response, 'delete')