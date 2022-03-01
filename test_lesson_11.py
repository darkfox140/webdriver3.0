from selenium.webdriver.support.ui import Select
from fixture.randdom_str import random_string
from fixture.config import browser


def test_l11(browser):
    account_info = dict(
        firstname=random_string("", 10),
        lastname=random_string("", 10),
        address1=random_string("", 10),
        postcode="12345",
        city=random_string("", 10),
        email=random_string("", 10) + "@fakegmail.org",
        phone="+71234567890",
        password="000000",
        confirmed_password="000000"
    )

    browser.get("http://localhost/litecart/")
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector("tr:last-of-type").click()

    for key, item in account_info.items():
        browser.find_element_by_name(key).send_keys(item)

    Select(browser.find_element_by_xpath("//select[@name='country_code']")).select_by_value("US")
    Select(browser.find_element_by_xpath("//select[@name='zone_code']")).select_by_value("CA")
    browser.find_element_by_xpath("//*[@name='create_account']").click()

    browser.find_element_by_xpath("//*[@id='box-account']//*[contains(text(), 'Logout')]").click()

    browser.find_element_by_xpath("//*[@name='email']").send_keys(account_info["email"])
    browser.find_element_by_xpath("//*[@name='password']").send_keys(account_info["password"])
    browser.find_element_by_xpath("//*[@name='login']").click()
    browser.find_element_by_css_selector("[href$='/logout']").click()
