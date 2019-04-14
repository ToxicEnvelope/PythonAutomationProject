#!/usr/bin/env python3
import unittest
from src.tests.base_test import BaseTest
from src.main.pageojects.signup_page import SignUpPage
from src.main.pageojects.account_page import AccountPage
from src.main.pageojects.login_page import LoginPage


class EnrollmentNewMemberTest(BaseTest, unittest.TestCase):

    # Test Data
    exp_greet_msg = "Hi, ספק יהב טסט"
    new_user = {
        "first": "Test",
        "last": "User",
        "phone": "0501116161",
        "email": "test2.user2@tu.com",
        "password": "Aa123456",
        "confpassword": "Aa123456"
    }

    # test create new member sign up scenario
    def test_1_new_member_enroll_and_logout(self):
        sp = SignUpPage(self.driver)
        ap = sp.register(
            fname=self.new_user['first'],
            lname=self.new_user['last'],
            phone=self.new_user['phone'],
            email=self.new_user['email'],
            password=self.new_user['password'],
            confpassword=self.new_user['confpassword']
        )
        self.assertTrue(isinstance(ap, AccountPage),
                        "Assert failed!\nexp: {0}\nact: {1}".format(AccountPage, type(ap)))
        lp = ap.logout()

        self.assertTrue(isinstance(lp, LoginPage),
                        "Assert failed!\nexp: {0}\nact: {1}".format(LoginPage, type(lp)))

    # test login with new created user and assert greetings message
    def test_2_login_with_new_created_member_and_assert_greetings(self):
        lp = LoginPage(self.driver)
        ap = lp.login(
            username=self.new_user['email'],
            password=self.new_user['password'],
            is_remember=True
        )
        msg = ap.get_greetings()

        self.assertEqual(msg, self.exp_greet_msg,
                         "Assert failed!\nexp: {0}\nact: {1}".format(self.exp_greet_msg, msg))


if __name__ == '__main__':
    unittest.main()
