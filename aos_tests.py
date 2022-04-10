from time import sleep
import unittest

import aos_methods
import aos_methods as methods
import aos_locators as locators


class AOSTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_account():
        methods.set_up()
        methods.create_new_account(locators.new_username, locators.new_password)
        methods.log_out(locators.new_username)
        methods.log_in(locators.new_username, locators.new_password)
        methods.log_out(locators.new_username)
        methods.tear_down()

    @staticmethod
    def test_validate_homepage_items():
        methods.set_up()
        sleep(2)
        aos_methods.validate_homepage_text()
        aos_methods.validate_nav_bar_links()
        aos_methods.validate_logo_is_displayed()
        aos_methods.contact_us()
        methods.tear_down()

    @staticmethod
    def test_validate_social_media_links():
        methods.set_up()
        sleep(2)
        methods.validate_social_media_links()
        methods.tear_down()
