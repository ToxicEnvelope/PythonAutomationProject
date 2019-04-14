#!/usr/bin/env python3
import unittest
from _src.main.config.global_config import GlobalConfig
from selenium import webdriver
from _src.main.utils.logger import Logger


class BaseTest(unittest.TestCase):
    logger = Logger(__name__)
    ROOT = GlobalConfig.get_bin_dir()
    driver = None

    def setUp(self):
        self.logger.info('{0} calling `setUp` method...'.format(__name__))
        self.driver = webdriver.Chrome(self.ROOT+"/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.logger.info('{0} calling `tearDown` method...'.format(__name__))
        if self.driver:
            self.driver.quit()