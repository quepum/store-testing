from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
