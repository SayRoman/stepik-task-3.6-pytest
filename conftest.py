import pytest
import importlib.util
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='Chrome',  # или default=None,
        help='Choose browser: Chrome, Firefox'
    )
    parser.addoption(
        '--language',
        action='store',
        default='ru, en',  # или default=None,
        help='Language'
    )

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    print(f'\nStart browser {browser_name} for test..')
    if browser_name == 'Firefox':
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(firefox_profile=options)
    elif browser_name == 'Chrome':
        print(f'\nStart browser {browser_name} for test..')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(5)

    yield driver

    print('\nQuit browser..')
    driver.quit()