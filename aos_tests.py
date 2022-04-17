from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import aos_methods as methods
import aos_locators as locators


class AOSTestCases(unittest.TestCase):
    chrome_service = Service('chromedriver.exe')

    def setUp(self):
        self.driver = webdriver.Chrome(service=self.chrome_service)
        methods.set_up(self.driver)

    def tearDown(self):
        methods.tear_down(self.driver)

    def test_create_new_account(self):
        new_user_info = locators.get_new_user()
        username = new_user_info[0]
        password = new_user_info[1]

        methods.create_new_account(self.driver, new_user_info)
        methods.log_out(self.driver, username)
        methods.log_in(self.driver, username, password)
        sleep(1)
        methods.validate_user_logged_in(self.driver, username)
        methods.log_out(self.driver, username)

    def test_validate_homepage_items(self):
        sleep(2)
        methods.validate_homepage_text(self.driver)
        methods.validate_nav_bar_links(self.driver)
        methods.validate_logo_is_displayed(self.driver)
        methods.contact_us(self.driver)

    def test_validate_social_media_links(self):
        sleep(2)
        methods.validate_social_media_links(self.driver)

    def test_delete_user_account(self):
        new_user_info = locators.get_new_user()

        methods.create_new_account(self.driver, new_user_info)
        methods.delete_user_account(self.driver, new_user_info)

    def test_checkout_shopping_cart(self):
        sleep(2)

        new_user_info = locators.get_new_user()

        methods.create_new_account(self.driver, new_user_info)
        methods.log_out(self.driver, new_user_info[0])

        methods.checkout_shopping_cart(self.driver, new_user_info)

        methods.delete_user_account(self.driver, new_user_info)
