import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from selene import browser

from befree_tests.contorls.utils import get_project_path


def load_env_credential():
    load_dotenv(dotenv_path=f'.env')


class BrowserSettings(BaseSettings):
    load_env_credential()
    window_width: str = '1600'
    window_height: str = '1028'
    email: str = os.getenv('email')

    def browser_option(self, context):
        load_dotenv(get_project_path() + '/.env')
        load_dotenv(get_project_path() + '/.env.stage')
        base_url = os.getenv('base_url')

        from selenium.webdriver.chrome.options import Options
        from selenium import webdriver
        options = Options()
        driver_options = webdriver.ChromeOptions()
        if context == 'bstack':
            selenoid_capabilities: dict = {
                "browserName": "chrome",
                "browserVersion": "122.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            user_name_capabilities = os.environ.get('user_name_capabilities')
            password_capabilities = os.environ.get('password_capabilities')
            options.capabilities.update(selenoid_capabilities)
            driver = webdriver.Remote(
                command_executor=f"https://{user_name_capabilities}:{password_capabilities}@selenoid.autotests.cloud/wd/hub",
                options=options)
            browser.config.driver = driver

        browser.config.driver_options = driver_options
        browser.config.base_url = base_url
        browser.config.window_width = self.window_width
        browser.config.window_height = self.window_height
        return options


config_browser = BrowserSettings()
