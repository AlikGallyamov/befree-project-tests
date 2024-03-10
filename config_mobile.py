import os
from typing import Optional

from pydantic_settings import BaseSettings

from befree_tests.contorls.utils import get_local_path_app


class SettingsMobile(BaseSettings):
    email: str = os.getenv('email')
    password: str = os.getenv('password')
    user_name: Optional[str] = os.getenv('user_name')
    access_key: Optional[str] = os.getenv('access_key')
    remote_url: str = os.getenv('remote_url')
    device_name: str = os.getenv('device_name')
    app_url: str = os.getenv('app_url', get_local_path_app())

    def to_driver_options(self, context):
        from appium.options.android import UiAutomator2Options
        options = UiAutomator2Options()

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', 'android')
            options.set_capability('platformVersion', '9.0')
            options.set_capability('app', self.app_url)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': os.getenv('user_name'),
                    'accessKey': os.getenv('access_key'),
                },
            )
        elif context == 'local_emulator':
            options.set_capability('platformName', 'android')
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('app', self.app_url)
            options.set_capability('appPackage', 'com.ddgcorp.befree')
            options.set_capability('noReset', 'false')
            options.set_capability('appWaitForLaunch', 'false')

        return options


config_mobile = SettingsMobile()
