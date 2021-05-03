from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.NAME, "registration-email")
    REGISTER_FORM_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_FORM_PASSWORD_REPEAT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR,
                            ".alert-success .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".content #content_inner")
    BASKET_PRODUCT_FORM = (By.CSS_SELECTOR, "#basket_summary")
