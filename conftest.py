import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language, for example: es, ru ")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    options = Options()
    user_browser = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print("i in --language")
    if user_browser=='chrome':
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif user_browser=='firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()