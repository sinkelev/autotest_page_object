from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_button_add_product(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART
        )
        add_to_cart_button.click()

    def price_comparison(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        price_in_cart = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_CART
        ).text
        assert product_price == price_in_cart, "Prices are not equal"

    def name_comparison(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_name_in_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_CART
        ).text
        assert product_name == product_name_in_cart, "Names are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented"

    def success_message_should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented"
