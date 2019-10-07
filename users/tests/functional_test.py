
from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase
import time
import os


class FunctionalTestProject(LiveServerTestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')


    def tearDown(self):
        self.driver.close()


    def test_github_login_and_logout_process(self):

        self.driver.get('http://127.0.0.1:8000/accounts/login/')
        time.sleep(0.5)

        # Click github login button
        self.driver.find_element_by_xpath('/html/body/main/div/div/div/form[1]/div/button').click()
        time.sleep(0.5)

        current_url = self.driver.current_url.split('?')[0]

        # Insert email & password credentials
        if current_url == 'https://github.com/login':

            self.driver.find_element_by_xpath('//*[@id="login_field"]')\
                .send_keys(os.getenv('GITHUB_EMAIL'))

            self.driver.find_element_by_xpath('//*[@id="password"]')\
                .send_keys(os.getenv('GITHUB_PASS'))

            self.driver.find_element_by_xpath(
                '/html/body/div[3]/main/div/form/div[2]/input[8]').click()
        else:
            self.fail(f'Unexpected url response: {self.driver.current_url}')


        current_url = self.driver.current_url.split('?')[0]
        if current_url == 'https://github.com/login/oauth/authorize':
            self.driver.find_element_by_xpath(
                '//*[@id="js-oauth-authorize-btn"]').click()

        # Test if authorisation redirects to home
        self.assertEquals('http://127.0.0.1:8000/', self.driver.current_url)
        time.sleep(0.5)

        # Test alert success message
        alert_success_msg = self.driver.find_element_by_xpath('/html/body/main/div/div/div[1]').text
        self.assertTrue(alert_success_msg,  alert_success_msg in 'Successfully')

        # Test welcome rendered response
        welcome_msg = self.driver.find_element_by_xpath('/html/body/main/div/div/div[2]/p').text
        self.assertTrue(welcome_msg, welcome_msg in 'Welcome')

        # Test navbar link (Profile)
        profile_text = self.driver.find_element_by_xpath('/html/body/header/nav/div/div/div[2]/a[1]').text
        self.assertTrue(profile_text, profile_text in 'Profile')

        # Tests logout flow
        self.driver.get('http://127.0.0.1:8000/accounts/logout/')
        time.sleep(0.5)

        self.driver.find_element_by_xpath('/html/body/main/div/div/form/button').click()
        text = self.driver.find_element_by_xpath('/html/body/main/div/div/div[1]').text
        self.assertTrue(text, text in 'signed out')





