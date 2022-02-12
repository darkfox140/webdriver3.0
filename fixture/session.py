import time

from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def init(self, app):
        self.app = app

    def field_email(self):
        # User name
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//*[contains(text(),'Username')]//following::input[@type='text']")

    def field_password(self):
        # Поле Пароль
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//*[contains(text(),'Password')]//following::input[@type='password']")

    def login_button(self):
        # Кнопка входа
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//*[contains(text(),'Login')]/self::button")

    def login(self, username, password):
        self.app.open_home_page()
        self.field_email().click()
        time.sleep(0.5)
        self.field_email().send_keys(username)
        self.field_password().click()
        time.sleep(0.5)
        self.field_password().send_keys(password)
        time.sleep(0.5)
        self.login_button().click()

    def logout(self):
        browser = self.app.browser
        browser.find_element(By.XPATH, "//i[@class='fa fa-sign-out fa-lg']").click()
        self.field_email()

    def ensure_logout(self):
        browser = self.app.browser
        if len(browser.find_elements(By.XPATH, "//*[contains(text(),'LiteCart® 1.3.7')]")) > 0:
            self.logout()

    def ensure_login(self, username, password):
        browser = self.app.browser
        if len(browser.find_elements(By.XPATH, "//i[@class='fa fa-sign-out fa-lg']")) > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//*[contains(text(),'LiteCart® 1.3.7')]").text
