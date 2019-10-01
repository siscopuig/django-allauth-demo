from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser, UserProfile
from django.contrib.auth.decorators import login_required


class TestViews(TestCase):


    # def setUp(self):
    #     self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
    #     self.profile1 = UserProfile.objects.update(user=self.user1, address='Street User1', phone_number='1234567890')
    #     self.user1.set_password('user1password')
    #     self.user1.save()

        # self.user2 = CustomUser.objects.create_user('user2@example.com', 'user2password')
        # self.pro2 = UserProfile.objects.update(user=self.user2, address='Street User2', phone_number='1234567890')
        # self.user2.set_password('user1password')
        # self.user2.save()


    # def test_signup_GET(self):
    #     resp = self.client.get(reverse('signup'))
    #     self.assertEquals(resp.status_code, 200)
    #     self.assertTemplateUsed(resp, 'signup.html')
    #
    #
    # def test_signup_user_POST(self):
    #     resp = self.client.post(reverse('signup'), {
    #         'email': 'user1@example.com',
    #         'password1': 'user1pass',
    #         'password2': 'user1pass'})
    #     self.assertEquals(resp.status_code, 200)
    #
    #
    # def test_login_GET(self):
    #     resp = self.client.get('/accounts/login/')
    #     self.assertEquals(resp.status_code, 200)
    #     self.assertTemplateUsed(resp, 'account/login.html')
    #
    #
    def test_login_user_POST(self):
        # self.client.login(username='user', password='test')  # defined in fixture or with factory in setUp()
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


    def test_call_view_fails_blank(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.user1.set_password('user1password')
        self.user1.save()
        resp = self.client.post('/accounts/login/', {}, follow=True)
        self.assertEquals(resp.status_code, 200)
        self.assertTrue(self.user1.is_authenticated)
    #
    #
    # def test_logout_GET(self):
    #     self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
    #     self.user1.set_password('user1password')
    #     self.user1.save()
    #
    #     resp = self.client.post('/accounts/login/', {'email': 'user1@example.com', 'password': 'user1password'}, follow=True)
    #     self.assertEquals(resp.status_code, 200)
    #     self.assertTrue(self.user1.is_authenticated)
    #
    #     resp = self.client.get('/accounts/logout/')
    #     self.assertRedirects(resp, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)


    # def test_profile_GET(self):
    #     self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
    #     self.user1.set_password('user1password')
    #     self.user1.save()
    #
    #     resp = self.client.post('/accounts/login/', {'email': 'user1@example.com', 'password': 'user1password'}, follow=True)
    #     self.assertEquals(resp.status_code, 200)
    #     self.assertTrue(self.user1.is_authenticated)
    #
    #     resp = self.client.get('/accounts/login/?next=/users/profile/')
    #     self.assertEquals(resp.status_code, 200)
    #
    #     resp = self.client.get(reverse('profile'))
    #     self.assertEquals(resp.status_code, 302)
    #
    #     self.assertTemplateUsed(resp, 'base.html')


    def test_delete_GET(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.user1.set_password('user1password')
        self.user1.save()


        # /accounts/login/?next=/users/profile/

# Run this test on terminal
# python manage.py test users.tests.test_views