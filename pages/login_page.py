from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Registration form is not presented"

    def register_new_user(self, email, password):
        enter_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        enter_email.send_keys(email)
        enter_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD
        )
        enter_password.send_keys(password)
        enter_password_repeat = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT
        )
        enter_password_repeat.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
