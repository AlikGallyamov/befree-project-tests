from selene import browser

from config import BrowserSettings

COOKIE_NAME = 'token'


class MainPage:
    env_data = BrowserSettings()

    def open_url(self):
        browser.open('/')

    def open_browser_with_cookie(self, response):
        browser.open('/').driver.add_cookie({"name": COOKIE_NAME, "value": response.json()['token']})
        browser.open('/')
