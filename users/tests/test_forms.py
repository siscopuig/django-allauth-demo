from users.forms import CustomUserProfile, CustomUserChangeForm
from users.models import UserProfile
from django.test import TestCase



class TestCustomUserForms(TestCase):
    
    def test_custom_user_profile_form(self):
        form = CustomUserProfile()    
        self.assertIn('name="address"', form.as_p())
        self.assertIn('name="phone_number"', form.as_p())
    
    def test_custom_user_change_form(self):
        form = CustomUserChangeForm()
        self.assertIn('name="first_name"', form.as_p())
        self.assertIn('name="last_name"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = CustomUserChangeForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
    