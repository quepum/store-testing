from pages.product_page import ProductPage
import pytest

product_base_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
product_page_link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
new_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    page.add_to_basket()
    page.should_be_added_to_basket()
    product_in_message = page.get_success_message()
    assert product_name == product_in_message, \
        f"Product name in message does not match expected"


@pytest.mark.xfail(reason="the user is not authorized")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, new_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, new_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="default")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, new_link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()
    assert "login" in page.browser.current_url, "Should be redirected to login page"
