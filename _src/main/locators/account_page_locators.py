
from selenium.webdriver.common.by import By


class AccountPageLocators:

    WELCOME_MSG = (By.CSS_SELECTOR, "h3.RTL")
    LAST_NAME_FIELD = (By.NAME, "lastname")
    RT_NAV_BER = (By.CSS_SELECTOR, "ul > ul.user_menu")
