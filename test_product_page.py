from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_add_product()
    page.solve_quiz_and_get_code()
    page.name_comparison()
    page.price_comparison()
    