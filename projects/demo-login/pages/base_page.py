from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def wait_for_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")

    def wait_for_visible(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not visible: {locator}")

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_visible(locator)
        return element.text

    def is_visible(self, locator, timeout=None):
        try:
            self.wait_for_visible(locator, timeout)
            return True
        except:
            return False

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
