from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import os


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Selenium Manager baixa o driver automaticamente
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_name = f"{scenario.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        context.driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot salvo: {screenshot_path}")

    if hasattr(context, 'driver'):
        context.driver.quit()
