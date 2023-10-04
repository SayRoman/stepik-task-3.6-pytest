import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_is_have_basket_button(browser):
    browser.get(link)
    is_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in is_language:
        time.sleep(30)
    find_buttons = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    assert len(find_buttons) > 0, 'Нет кнопки добавления в корзину'
