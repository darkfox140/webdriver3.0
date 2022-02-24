import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_lesson_8(browser):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(10)
    products = browser.find_elements(By.XPATH, "//*[@class='image-wrapper']")
    for products in products:
        stickers = products.find_elements(By.CSS_SELECTOR, ".sticker")
        assert len(stickers) == 1
