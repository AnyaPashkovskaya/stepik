from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver 
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url# current url for user
        print(" current_url:", current_url)
        assert 'login' in current_url, 'the current link does not match the expected:'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"

    def register_new_user(self, email, password):
        registr_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registr_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registr_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registr_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registr_email.send_keys(email)
        registr_password1.send_keys(password)
        registr_password2.send_keys(password)
        registr_button.click()




