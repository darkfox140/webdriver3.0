from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_l14(browser):
    browser.get("http://localhost/litecart/admin/")
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()
    wait = WebDriverWait(browser, 10)

    browser.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    browser.find_element_by_xpath("//*[@class='row']//a").click()

    main_window = browser.current_window_handle
    links = browser.find_elements_by_xpath("//*[@class='fa fa-external-link']")

    for link in links:
        link.click()
        new_window = [i for i in browser.window_handles if i != main_window]
        wait.until(EC.new_window_is_opened(new_window))

        for window in new_window:
            browser.switch_to.window(window)
            browser.close()
        browser.switch_to.window(main_window)
