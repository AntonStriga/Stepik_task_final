from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_SUMMARY), "There are products in the basket"

    def should_message_basket_is_empty(self):
        assert self.is_element_present(*BasketLocators.MESSAGE_BASKET_IS_EMPTY), "The message basket empty is missing"


