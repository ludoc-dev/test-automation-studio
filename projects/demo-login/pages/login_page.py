from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")
        self.logout_button = (By.CSS_SELECTOR, "a[href='/logout']")
        self.success_indicator = (By.CSS_SELECTOR, ".success")
        self.error_indicator = (By.CSS_SELECTOR, ".error")

    def open(self):
        self.navigate(self.url)
        return self

    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)
        return self

    def get_flash_message(self):
        return self.get_text(self.flash_message).strip()

    def is_login_successful(self):
        return self.is_visible(self.success_indicator, timeout=5)

    def is_login_failed(self):
        return self.is_visible(self.error_indicator, timeout=5)

    def logout(self):
        if self.is_visible(self.logout_button, timeout=2):
            self.click(self.logout_button)
        return self
