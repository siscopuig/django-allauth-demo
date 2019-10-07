from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

# To run this test on terminal
# $ python manage.py test users.tests.test_views

class TestViews(TestCase):

    def test_signup_render_template(self):
        resp = self.client.get(reverse('signup'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'signup.html')


    def test_login_render_template(self):
        resp = self.client.get('/accounts/login/')
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'account/login.html')


    def test_logout_redirect_to_home(self):
        resp = self.client.get('/accounts/logout/')
        self.assertRedirects(resp, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)


    def test_profile_render_template(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.user1.set_password('user1password')
        self.user1.save()
        self.client.login(username='user1@example.com', password='user1password')
        resp = self.client.get(reverse('profile'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'profile.html')


    def test_delete_redirect_to_signup(self):
        self.user1 = CustomUser.objects.create_user('user1@example.com', 'user1password', is_active=True)
        self.user1.set_password('user1password')
        self.user1.save()
        self.client.login(username='user1@example.com', password='user1password')
        resp = self.client.get(reverse('delete'))
        self.assertRedirects(resp, '/users/signup/', status_code=302, target_status_code=200, fetch_redirect_response=True)