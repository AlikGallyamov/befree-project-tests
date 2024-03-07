from dotenv import load_dotenv
import pytest
from selene import browser
from befree_tests.contorls import attach
from config import config_browser


@pytest.fixture(autouse=False)
def browser_settings():
    config_browser()

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
