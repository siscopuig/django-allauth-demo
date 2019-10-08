
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import LiveServerTestCase
import time
import os


MAX_WAIT = 5


def custom_wait_for(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return func(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return wrapper
            


class FunctionalTestProject(LiveServerTestCase):
    """
    Test social account login process locally.
    """

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    def tearDown(self):
        self.driver.close()
    
    @custom_wait_for
    def test_social_account_login_flow(self):

        self.driver.get('http://127.0.0.1:8000/accounts/login/')

        # Click github login button
        self.driver.find_element_by_xpath(
          '/html/body/main/div/div/div/form[1]/div/button').click()
        
        # Removes string characters after question mark
        current_url = self.driver.current_url.split('?')[0]

        # Send keys to email & password placeholders
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
            self.driver.find_element_by_xpath('//*[@id="js-oauth-authorize-btn"]').click()

            # Test if authorisation redirects to home
            self.assertEquals('http://127.0.0.1:8000/', self.driver.current_url)
            
        if current_url == 'https://github.com/sessions/verified-device':
            self.assertTrue(current_url, current_url in 'verified-device') 





