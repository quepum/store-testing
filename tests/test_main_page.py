﻿from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "https://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    assert page.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present."
