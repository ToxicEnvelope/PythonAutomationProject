from selenium.webdriver.common.by import By

class SignUpPageLocators:

    FIRST_NAME_FIELD = (By.NAME, "firstname")
    LAST_NAME_FIELD = (By.NAME, "lastname")
    MOBILE_NUMBER_FIELD = (By.NAME, "phone")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_FIELD = (By.NAME, "confirmpassword")
    SIGN_UP_BTN = (By.CSS_SELECTOR, "button.signupbtn")
    EXISTS_ERROR = (By.CSS_SELECTOR, "div.alert-danger")
