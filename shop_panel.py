import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get("http://localhost/litecart/en/")
    browser.find_elements(By.CSS_SELECTOR, "li[class='product column shadow hover-light']")
    for element in browser.find_elements(By.CSS_SELECTOR, "li[class='product column shadow hover-light']"):
        assert element.find_element(By.CSS_SELECTOR, "div[class*='sticker']") is not None, "Стикер отсутствует!!!"
finally:
    time.sleep(5)
    browser.quit()
