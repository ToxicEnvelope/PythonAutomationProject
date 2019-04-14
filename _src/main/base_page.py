#!/usr/bin/env python3
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException, TimeoutException
from _src.main.utils.logger import Logger

class BasePage:

    BASE_URL = "https://www.phptravels.net"
    _driver = None

    '''
        CONSTRUCTOR
        :param -> driver : WebDriver
    '''
    def __init__(self, driver, namespace):
        try:
            self.logger = Logger(namespace)
            if isinstance(driver, WebDriver):
                self._driver = driver
                self.logger.info('{0} - __init__ -> {1}'.format(namespace, self._driver))
        except Exception as err:
            raise err

    '''
        CLICK FUNCTION
        :param -> element : WebElement
    '''
    def click(self, element):
        self.logger.info('click -> '+ str(element))
        try:
            if isinstance(element, WebElement):
                self.logger.debug('isntanceof' + str(element))
                if element.is_displayed():
                    self.logger.debug('is displayed '+ str(element.is_displayed()))
                    element.click()
        except (Exception, WebDriverException,
                StaleElementReferenceException) as err:
            self.logger.error(err)
            raise err

    '''
        CLEAR SEND KEYS FUNCTION
        :param -> element : WebElement
        :param -> phrase : String
    '''
    def clear_send_keys(self, element, phrase):
        self.logger.info('clear_send_keys -> '+ str(element) +' : '+str(phrase))
        try:
            if element.is_displayed():
                self.logger.debug('is displayed '+ str(element.is_displayed()))
                element.clear()
                self.logger.debug('send_keys -> '+str(element)+ " : "+str(phrase))
                element.send_keys(phrase)
        except (Exception, WebDriverException,
                StaleElementReferenceException) as err:
            self.logger.error(err)
            raise err

    '''
        WAIT FUNCTION
        :param -> sec=5 : Integer        
    '''
    def wait(self, sec=5):
        self.logger.info('wait -> '+ str(sec))
        try:
            sleep(sec)
        except Exception as err:
            self.logger.error(err)
            raise err

    """
        SMART WAIT CLICK
    """
    def wait_click(self, tpl_elem):
        self.logger.info('wait_click -> '+ str(tpl_elem))
        try:
            self.logger.debug('waiting for element...')
            elem = WebDriverWait(self._driver, 15, 0.3)\
                .until(EC.visibility_of_element_located(tpl_elem))
            self.logger.debug('found ? ' + str(elem))
            if elem is not None\
                    and elem.is_displayed():
                self.logger.debug('click -> '+ str(elem))
                elem.click()
        except (Exception, WebDriverWait,
                StaleElementReferenceException) as err:
            self.logger.error(err)
            raise err

    """
        SMART WAIT SEND KEYS
    """
    def wait_clear_send_keys(self, tpl_elem, phrase):
        self.logger.info('wait_clear_send_keys -> '+str(tpl_elem)+' : '+str(phrase))
        try:
            self.logger.debug('waiting for element...')
            elem = WebDriverWait(self._driver, 10, 0.3)\
                .until(EC.visibility_of_element_located(tpl_elem))
            self.logger.debug('found ? ' + str(elem))
            if elem is not None\
                    and elem.is_displayed():
                self.logger.debug('clear...')
                elem.clear()
                self.logger.debug('send_keys -> '+str(elem)+' : '+str(phrase))
                elem.send_keys(phrase)
        except (Exception, WebDriverException,
                StaleElementReferenceException) as err:
            self.logger.error(err)
            raise err

    """
        WAIT FOR ELEMENT
    """
    def wait_for_webelement(self, tpl_elem):
        self.logger.info('wait_for_webelement -> '+ str(tpl_elem))
        try:
            self.wait()
            self.logger.debug('waiting for element...')
            return WebDriverWait(self._driver, 15, 0.3)\
                .until(EC.visibility_of_element_located(tpl_elem))
        except (Exception, WebDriverException,
                StaleElementReferenceException) as err:
            self.logger.error(err)
            raise err


    def wait_until_page_loaded(self, title):
        self.logger.info('wait_until_page_loaded -> '+title)
        try:
            self.logger.debug('waiting for page...')
            html_page = WebDriverWait(self._driver, 5, 0.25)\
                .until(EC.title_is(title))
            self.logger.debug('found page ' + str(html_page))
        except (Exception, TimeoutException) as te:
            self.logger.error(te)
            raise te

    def navigate_to(self, url):
        self.logger.info('navigate_to -> ' + url)
        try:
            self._driver.get(url)
        except (Exception, TimeoutException) as te:
            self.logger.error(te)
            raise te

    """
        INIT ELEMENTS AS ABSTRACT METHOD
    """
    def init_elements(self): pass
