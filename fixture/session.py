from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        browser = self.app.browser
        self.app.open_home_page()
        browser.find_element(By.NAME, "username").clear()
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "password").clear()
        browser.find_element(By.NAME, "password").send_keys(password)
        browser.find_element(By.XPATH, "//*[contains(text(),'Login')]/self::button").click()

    def logout(self):
        browser = self.app.browser
        browser.find_element(By.XPATH, "//i[@class='fa fa-sign-out fa-lg']t").click()
        browser.find_element(By.NAME, "username")

    def ensure_logout(self):
        browser = self.app.browser
        if len(browser.find_elements(By.XPATH, "//i[@class='fa fa-sign-out fa-lg']t")) > 0:
            self.logout()

    def ensure_login(self, username, password):
        browser = self.app.browser
        if len(browser.find_elements(By.XPATH, "//i[@class='fa fa-sign-out fa-lg']t")) > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        browser = self.app.browser
        return self.get_logged_user() == username

    def get_logged_user(self):
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//*[contains(text(),'LiteCart® 1.3.7')]").text
