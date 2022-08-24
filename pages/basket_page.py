from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM), "Product is presented in cart"


    def should_be_message_no_products(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_NO_PRODUCTS), "No product message is not presented"
