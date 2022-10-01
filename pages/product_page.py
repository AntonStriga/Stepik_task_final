from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_message_product_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is not presented"

    def message_contains_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "The message does not contain the product name"

    def should_message_cost_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message basket total is not presented"

    def cost_basket_is_equal_price_product(self):
        cost_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cost_basket == price_product, "Product price and basket price is not equal"

    def add_product_to_basket(self):
        self.should_message_product_added_to_cart()
        self.message_contains_name_product()
        self.should_message_cost_basket()
        self.cost_basket_is_equal_price_product()

