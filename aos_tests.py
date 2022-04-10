import unittest
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
