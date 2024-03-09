import os

from dotenv import load_dotenv

from pydantic_settings import BaseSettings
from selenium.webdriver.chrome.options import Options
from selene import browser
from selenium import webdriver


def load_env_credential():
    load_dotenv(dotenv_path=f'.env')


def load_env_stage():
    load_dotenv(dotenv_path=f'.env.stage')


class BrowserSettings(BaseSettings):
    load_env_stage()
    load_env_credential()
    window_width: str = '1900'
    window_height: str = '1028'
    email: str = os.getenv('email')
    password: str = os.getenv('password')
    base_url: str = os.getenv('base_url')
    back_url: str = os.getenv('auth_url')
    catalog_url: str = os.getenv('catalog_url')


def config_browser():
    config = BrowserSettings()
    options = Options()
    driver_options = webdriver.ChromeOptions()

    browser.config.driver_options = driver_options
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
