from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_lesson_7(browser):
    browser.get("http://localhost/litecart/admin/")
    browser.find_element(By.NAME, "username").send_keys("admin")
    browser.find_element(By.NAME, "password").send_keys("admin")
    browser.find_element(By.NAME, "login").click()
    wait = WebDriverWait(browser, 10)

    menu_number = len(browser.find_elements(By.XPATH, "//*[@id='app-']"))

    while menu_number:
        menu_number -= 1
        menu_items = browser.find_elements(By.XPATH, "//*[@id='app-']")
        menu_items[menu_number].click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))

        submenu_number = len(browser.find_elements(By.XPATH, "//*[@class='docs']/li/a"))

        while submenu_number:
            submenu_number -= 1
            submenu_items = browser.find_elements(By.XPATH, "//*[@class='docs']/li/a")
            submenu_items[submenu_number].click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))

            EC.number_of_windows_to_be(1)
