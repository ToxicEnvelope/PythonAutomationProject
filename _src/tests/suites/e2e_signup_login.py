import unittest
from _src.tests.single.signup_page_test import SignUpPageTest
from _src.tests.single.login_page_test import LoginPageTest


def suite():

    suites = [
            SignUpPageTest('test_exists_user_register'),
            SignUpPageTest('test_new_user_register'),
            LoginPageTest('test_user_invalid_login'),
            LoginPageTest('test_user_valid_login'),
            LoginPageTest('test_invalid_user_forgot_password')
    ]
    s = unittest.TestSuite()
    s.addTests(suites)
    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    # payload_tests = suite()
    runner.run(suite())
    # runner.run(payload_tests)
