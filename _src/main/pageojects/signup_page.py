#!/usr/bin/env python3
from _src.main.base_page import BasePage
from _src.main.locators.signup_page_locator import SignUpPageLocators

class SignUpPage(BasePage, SignUpPageLocators):


    def __init__(self, driver):
        self.logger.info('{0} - __init__ -> {1}'.format(__name__, driver))
        super(SignUpPage, self).__init__(driver)
        self.URL = self.BASE_URL + "/register"
        self.logger.debug('page url -> {0}'.format(self.URL))
        self.navigate_to(self.URL)
        self.wait_until_page_loaded(self._driver.title)


    def register(self, fname, lname, phone, email, password, confpassword):
        self.logger.info('{0} : register'.format(__name__))
        try:
            self.wait_clear_send_keys(self.FIRST_NAME_FIELD,fname)
            self.wait_clear_send_keys(self.LAST_NAME_FIELD, lname)
            self.wait_clear_send_keys(self.MOBILE_NUMBER_FIELD, phone)
            self.wait_clear_send_keys(self.EMAIL_FIELD, email)
            self.wait_clear_send_keys(self.PASSWORD_FIELD, password)
            self.wait_clear_send_keys(self.CONFIRM_FIELD, confpassword)
            self.wait_click(self.SIGN_UP_BTN)
        except:
            self.logger.error('{0} -> register'.format(__name__))
            raise

    def get_err_msg(self):
        self.logger.info('{0} : get_err_msg'.format(__name__))
        try:
            err = self.wait_for_webelement(self.EXISTS_ERROR)
            self.logger.debug('found ? ' + str(err))
            return err.text
        except:
            self.logger.error('{0} -> get_err_msg'.format(__name__))
            raise
