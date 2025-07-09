from pages.product_page import ProductPage

link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    page.add_to_basket()
    page.should_be_added_to_basket()
    product_in_message = page.get_success_message()
    assert product_name in product_in_message, \
        f"Product name in message '{product_in_message}' does not match expected '{product_name}'"
