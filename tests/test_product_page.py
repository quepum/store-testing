from pages.product_page import ProductPage
import pytest

product_base_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


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
