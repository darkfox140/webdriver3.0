import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def add_to_cart(browser, count=1):
    for i in range(count):
        browser.find_element_by_xpath("//*[@id='box-most-popular']//a[@class='link']").click()
        browser.find_element_by_xpath("//*[@name='add_cart_product']").click()
        counter = int(browser.find_element_by_xpath("//span[@class='quantity']").text)
        WebDriverWait(browser, 10).until(lambda s: int(s.find_element_by_xpath("//span[@class='quantity']").text) == counter+1)
        browser.back()


def del_from_cart(browser):
    browser.find_element_by_xpath("//*[@id='cart']/a[@class='link']").click()
    counter = len(browser.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
    while counter > 0:
        browser.find_element_by_xpath("//*[@name='remove_cart_item']").click()
        WebDriverWait(browser, 10).until(lambda s: len(s.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr")) < counter)
        counter = len(browser.find_elements_by_xpath("//table[contains(@class, 'dataTable')]//tr"))
    browser.back()


def test_l13(browser):
    browser.get("http://localhost/litecart/en/")
    WebDriverWait(browser, 10)

    add_to_cart(browser, 3)
    del_from_cart(browser)
