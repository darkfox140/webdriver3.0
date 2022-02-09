import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver(request):
    web_browser = webdriver.Chrome()
    request.addfinalizer(web_browser.quit)
    return web_browser


def test_proba(driver):
    driver.get("http://suninjuly.github.io/wait1.html")
    driver.implicitly_wait(5)
    button = driver.find_element(By.ID, "verify")
    button.click()
    message = driver.find_element(By.ID, "verify_message")
    assert "successful" in message.text