import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--lang={user_language}")
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name is not correct. Use 'chrome' or 'firefox'.")

    yield driver
    driver.quit()