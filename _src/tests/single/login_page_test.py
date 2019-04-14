#!/usr/bin/env python3
import unittest
from _src.tests.base_test import BaseTest
from _src.main.pageojects.login_page import LoginPage
from _src.main.pageojects.account_page import AccountPage


class LoginPageTest(BaseTest, unittest.TestCase):

    # Test Data
    valid_user = ("test1@aut.com", "Aa123456")
    invalid_user = ("admin@support.com", "Password1")
    exp_err_login_msg = "Invalid Email or Password"
    exp_err_forget_msg = "Email Not Found"
    exp_greet_msg = "Hi, {0} {1}".format("test", "user1")

    # test a invalid user login scenario
    def test_user_invalid_login(self):
        try:
            self.logger.info('{0} calling `test_user_invalid_login` method...'.format(__name__))
            lp = LoginPage(self.driver)
            lp.login(self.invalid_user[0], self.invalid_user[1], True)
            err_msg = lp.get_login_error_mgs()

            self.assertEqual(err_msg, self.exp_err_login_msg,
                             "Assert failed:\nexpects: {0}\nactual: {1}".format(self.exp_err_login_msg, err_msg))
        finally:
            self.logger.info('{0} `test_user_invalid_login` - test end'.format(__name__))

    # test a valid user login scenario
    def test_user_valid_login(self):
        try:
            self.logger.info('{0} calling `test_user_valid_login` method...'.format(__name__))

            lp = LoginPage(self.driver)
            lp.login(self.valid_user[0], self.valid_user[1], False)

            msg = lp.get_success_msg()
            print(msg)

            ap = AccountPage(self.driver)
            greet = ap.get_greetings()
            self.assertEqual(greet, self.exp_greet_msg,
                             "Assert failed:\nexpects: {1}\nactual: {0}".format(greet, self.exp_greet_msg))
        finally:
            self.logger.info('{0} `test_user_valid_login` - test end'.format(__name__))

    # test a invalid user forgot password scenario
    def test_invalid_user_forgot_password(self):
        try:
            self.logger.info('{0} calling `test_invalid_user_forgot_password` method...'.format(__name__))

            lp = LoginPage(self.driver)
            lp.forget_password(self.invalid_user[0])

            msg = lp.get_error_msg()

            self.assertEqual(msg, self.exp_err_forget_msg,
                             "Assert failed:\nexpects: {1}\nactual: {0}".format(msg, self.exp_err_forget_msg))
        finally:
            self.logger.info('{0} `test_invalid_user_forgot_password` - test end'.format(__name__))


if __name__ == '__main__':
    unittest.main()
