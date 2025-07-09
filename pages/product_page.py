from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message(self):
        full_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

        clean_text = full_text.replace("×", "").strip()

        if "has been added" in clean_text:
            clean_text = clean_text.split("has been added")[0].strip()

        return clean_text

    def get_basket_total(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should"

    def should_be_added_to_basket(self):
        assert self.get_product_name() in self.get_success_message(), \
            f"Название товара в корзине не совпадает ({self.get_product_name()}, {self.get_success_message()})"

        assert self.get_product_price() in self.get_basket_total(), \
            f"Цена товара {self.get_product_price()} и сумма корзины {self.get_basket_total()} не совпадают"
