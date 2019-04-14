#!/usr/bin/env python3
from _src.main.base_page import BasePage
from _src.main.locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage, AccountPageLocators):

    def __init__(self, driver):
        self.logger.info('{0} - __init__ -> {1}'.format(__name__, driver))
        super(AccountPage, self).__init__(driver)
        self.URL = self.BASE_URL + "/account"
        self.logger.debug('page url -> {0}'.format(self.URL))
        self.navigate_to(self.URL)
        self.wait_until_page_loaded(self._driver.title)

    def get_greetings(self):
        self.logger.info('{0} : get_greetings'.format(__name__))
        try:
            self.logger.debug('waiting for element...')
            elem = self.wait_for_webelement(self.WELCOME_MSG)
            self.logger.debug('found ? '+ str(elem))
            return elem.text
        except:
            self.logger.error('{0} -> get_greetings'.format(__name__))
            raise

    def logout(self):
        self.logger.info('{0} : logout'.format(__name__))
        try:
            self.wait_click(self.RT_NAV_BER)
            elem = self.wait_for_webelement(self.WELCOME_MSG)
            self.logger.debug('found ? '+ str(elem))
            elem.find_element_by_link_text("Logout").click()
        except:
            self.logger.error('{0} -> logout'.format(__name__))
            raise

