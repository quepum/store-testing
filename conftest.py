import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose interface language, e.g. 'en', 'ru', 'es'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    # Настройки локализации
    options = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--lang={user_language}")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
    else:
        raise pytest.UsageError("--browser_name is not correct. Use 'chrome' or 'firefox'.")

    print(f"\nStarting {browser_name} browser with language '{user_language}'...")
    driver = webdriver.Chrome(options=options) if browser_name == "chrome" \
        else webdriver.Firefox(options=options)

    yield driver

    print("\nQuit browser...")
    driver.quit()