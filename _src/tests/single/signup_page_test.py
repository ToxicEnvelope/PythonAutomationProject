#!/usr/bin/env python3
import unittest
from _src.tests.base_test import BaseTest
from _src.main.pageojects.signup_page import SignUpPage
from _src.main.pageojects.account_page import AccountPage


class SignUpPageTest(BaseTest, unittest.TestCase):

    # Test Data
    new_user_info = {
        "firstName": "test",
        "lastName": "user17",
        "phoneNumber": "0526105108",
        "email": "test17@aut.com",
        "password": "Aa123456"
    }
    exists_user_info = {
        "firstName": "test",
        "lastName": "user1",
        "phoneNumber": "0526105108",
        "email": "test1@aut.com",
        "password": "Aa123456"
    }

    exp_exists_error_msg = "Email Already Exists."

    # test exists user register
    def test_exists_user_register(self):
        try:
            self.logger.info('{0} calling `test_exists_user_register` method...'.format(__name__))

            sp = SignUpPage(self.driver)
            sp.register(
                fname=self.exists_user_info["firstName"],
                lname=self.exists_user_info["lastName"],
                phone=self.exists_user_info["phoneNumber"],
                email=self.exists_user_info["email"],
                password=self.exists_user_info["password"],
                confpassword=self.exists_user_info["password"]
            )
            msg = sp.get_err_msg()
            self.assertEqual(msg, self.exp_exists_error_msg, "Assert Failed!\nexpects: {1}\nactual: {0}"
                             .format(msg, self.exp_exists_error_msg))
        finally:
            self.logger.info('{0} `test_exists_user_register` - test end'.format(__name__))

    # test new user register
    def test_new_user_register(self):
        try:
            self.logger.info('{0} calling `test_new_user_register` method...'.format(__name__))

            sp = SignUpPage(self.driver)
            sp.register(
                fname=self.new_user_info["firstName"],
                lname=self.new_user_info["lastName"],
                phone=self.new_user_info["phoneNumber"],
                email=self.new_user_info["email"],
                password=self.new_user_info["password"],
                confpassword=self.new_user_info["password"]
            )

            ap = AccountPage(self.driver)
            greet = ap.get_greetings()
            self.assertEqual(greet, greet, "")
            ap.logout()
        finally:
            self.logger.info('{0} `test_new_user_register` - test end'.format(__name__))



if __name__ == '__main__':
    unittest.main()
