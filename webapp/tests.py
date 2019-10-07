
from django.test import TestCase

class HomePageTest(TestCase):

    def test_home_render_template(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'home.html')