#!/usr/bin/env python3
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # URL
    URL = "login"
    # Login Form
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    REMEMBER_CHECKBOX = (By.ID, "remember-me")
    # Page Buttons
    LOGIN_BTN = (By.CSS_SELECTOR, "button.loginbtn")
    SIGN_UP_BTN = (By.CSS_SELECTOR, "a.form-group")
    FORGOT_BTN = (By.CSS_SELECTOR, "a[data-toggle='modal']")
    # Forget Layout
    FORGET_EMAIL_FIELD = (By.ID, "resetemail")
    FORGET_RESET_BTN = (By.CSS_SELECTOR, "button.resetbtn")
    FORGET_CLOSE_BTN = (By.CSS_SELECTOR, "button.close")
    # Errors
    FORGET_ERR_DIV = (By.CSS_SELECTOR, "div.alert-danger")
    LOGIN_ERR_DIV = (By.CSS_SELECTOR, "div.alert-danger")
    # Success
    FORGET_SUCCESS_DIV = (By.CSS_SELECTOR, "div.alert-success")

