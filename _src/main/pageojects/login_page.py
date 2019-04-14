#!/usr/bin/env python3
from _src.main.base_page import BasePage
from _src.main.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):

    def __init__(self, driver):
        self.logger.info('{0} - __init__ -> {1}'.format(__name__, driver))
        super(LoginPage, self).__init__(driver)
        self.URL = '{domain}/{uri}'.format(domain=self.BASE_URL, uri=self.URL)
        self.logger.debug('page url -> {0}'.format(self.URL))
        self.navigate_to(self.URL)
        self.wait_until_page_loaded(self._driver.title)

    """
        login
    """
    def login(self, username, password, is_remember):
        self.logger.info('{0} : login'.format(__name__))
        try:
            self.logger.debug('check remember ? ' + str(is_remember))
            if not is_remember:
                self.wait_clear_send_keys(self.USERNAME_FIELD, username)
                self.wait_clear_send_keys(self.PASSWORD_FIELD, password)
                self.wait_click(self.LOGIN_BTN)
            else:
                self.wait_clear_send_keys(self.USERNAME_FIELD, username)
                self.wait_clear_send_keys(self.PASSWORD_FIELD, password)
                self.wait_click(self.REMEMBER_CHECKBOX)
                self.wait_click(self.LOGIN_BTN)
        except:
            self.logger.error('{0} -> login'.format(__name__))
            raise

    def get_login_error_mgs(self):
        self.logger.info('{0} : get_login_error_mgs'.format(__name__))
        try:
            err_elem = self.wait_for_webelement(self.LOGIN_ERR_DIV)
            self.logger.debug('found ? ' + str(err_elem))
            if err_elem:
                return err_elem.text
        except:
            self.logger.error('{0} -> get_login_error_mgs'.format(__name__))
            raise
    """
        signup
    """
    def sign_up(self):
        self.logger.info('{0} : sign_up'.format(__name__))
        try:
            self.wait_click(self.SIGN_UP_BTN)
        except:
            self.logger.error('{0} -> sign_up'.format(__name__))
            raise

    """
        forget password
    """
    def forget_password(self, email):
        self.logger.info('{0} : forget_password'.format(__name__))
        try:
            self.wait_click(self.FORGOT_BTN)
            self.wait_clear_send_keys(self.FORGET_EMAIL_FIELD, email)
            self.wait_click(self.FORGET_RESET_BTN)
        except:
            self.logger.error('{0} -> forget_password'.format(__name__))
            raise

    def get_error_msg(self):
        self.logger.info('{0} : get_error_msg'.format(__name__))
        try:
            err_msg = self.wait_for_webelement(self.FORGET_ERR_DIV)
            self.logger.debug('found ? ' + str(err_msg))
            if err_msg.is_displayed():
                txt = err_msg.text
                self.wait_click(self.FORGET_CLOSE_BTN)
                self.logger.debug('found text -> ' + str(txt))
                return txt
        except:
            self.logger.error('{0} -> get_error_msg'.format(__name__))
            raise

    def get_success_msg(self):
        self.logger.info('{0} : get_success_msg'.format(__name__))
        try:
            suc_msg = self.wait_for_webelement(self.FORGET_SUCCESS_DIV)
            self.logger.debug('found ? '+ str(suc_msg))
            if suc_msg.is_displayed():
                txt = suc_msg.text
                self.wait_click(self.FORGET_CLOSE_BTN)
                self.logger.debug('found text -> ' + str(txt))
                return txt
        except:
            self.logger.error('{0} -> get_success_msg'.format(__name__))
            raise


if __name__ == '__main__':
    from selenium import webdriver
    from os.path import expanduser

    PROJ_DIR = expanduser("~/Desktop/Git/NewPythonProject")

    driver = webdriver.Chrome("{0}/bin/chromedriver.exe".format(PROJ_DIR))
    driver.maximize_window()

    driver.get("https://www.phptravels.net/login")

    lp = LoginPage(driver)

    td_user = "Admin"
    td_pwd = "Password1"
    exp_err_msg = "Invalid Email or Password123"

    # This is an INVALID Test
    lp.login(td_user, td_pwd, True)
