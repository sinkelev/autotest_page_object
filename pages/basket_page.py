from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Empty basket message is not presented"

    def should_be_empty_basket_form(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_FORM), \
            "Basket form is presented"
