from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_message_product_added_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "The product name is not present"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "The message does not contain the product name"

    def should_message_cost_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message basket total is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "The price of the product is not presented"
        cost_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cost_basket == price_product, "Product price and basket price is not equal"


