from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET =[By.CSS_SELECTOR, ".btn-group"]

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = [By.CSS_SELECTOR, ".btn-add-to-basket"]
    MESSAGE_ABOUT_ADDING = [By.CSS_SELECTOR, "#messages div:nth-child(1) strong"]
    PRODUCT_NAME = [By.CSS_SELECTOR, "div.product_main h1"]
    MESSAGE_BASKET_TOTAL = [By.CSS_SELECTOR, ".alert-info .alertinner strong"]
    PRODUCT_PRICE = [By.CSS_SELECTOR, ".product_main .price_color"]
    SUCCESS_MESSAGE = [By.CSS_SELECTOR, "#messages div:nth-child(1)"]

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketLocators():
    BASKET_SUMMARY = [By.CSS_SELECTOR, ".basket_summary"]
    MESSAGE_BASKET_IS_EMPTY = [By.CSS_SELECTOR, "#content_inner"]








