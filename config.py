import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from selene import browser

from befree_tests.contorls.utils import get_local_path_app


def load_env_stage():
    load_dotenv(dotenv_path=f'.env.stage')


def load_env(context):
    load_dotenv(dotenv_path=f'.env.{context}')


def load_env_credential():
    load_dotenv(dotenv_path=f'.env')


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
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    config = BrowserSettings()
    options = Options()
    driver_options = webdriver.ChromeOptions()

    browser.config.driver_options = driver_options
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height


class SettingsMobile(BaseSettings):
    user_name: Optional[str] = os.getenv('user_name')
    access_key: Optional[str] = os.getenv('access_key')
    remote_url: str = os.getenv('remote_url')
    device_name: str = os.getenv('device_name')
    app_url: str = os.getenv('app_url', get_local_path_app())


def config_mobile(context):
    from appium.options.android import UiAutomator2Options
    from appium import webdriver

    if context == 'bstack':
        load_env_credential()
        load_env(context)
        config = SettingsMobile()
        device_capabilities = {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": config.device_name,
            "app": config.app_url,

            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": f"{config.user_name}",
                "accessKey": f"{config.access_key}"
            }
        }

    if context == 'local_emulator':
        load_env(context)
        config = SettingsMobile()
        device_capabilities = {
            "platformName": "android",
            "appium:automationName": "UiAutomator2",
            "appium:ignoreHiddenApiPolicyError": "true",
            "appium:app": config.app_url,
            "appium:deviceName": config.device_name,
            "appium:appWaitActivity": "org.wikipedia.*",
            "appium:noReset": "false"
        }

    options = UiAutomator2Options().load_capabilities(device_capabilities)
    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options
    )
    return context
