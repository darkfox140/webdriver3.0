from fixture.config import browser
from selenium.webdriver.common.by import By


def test_lesson_8(browser):
    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(10)
    products = browser.find_elements(By.XPATH, "//*[@class='image-wrapper']")
    for product in products:
        #stickers = product.find_elements(By.XPATH, "//*[contains(@class, 'sticker')]")
        stickers = product.find_elements(By.CSS_SELECTOR, ".sticker")
        assert len(stickers) == 1
