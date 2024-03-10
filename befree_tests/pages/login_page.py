import os
import time

import allure
from appium.webdriver.common.appiumby import AppiumBy

from selene import browser, have


class LoginPage:
    email = os.environ.get("email")
    password = os.environ.get("password")

    def open_page(self):
        time.sleep(5)
        with allure.step("Кликаем по иконке профиля"):
            browser.element((AppiumBy.XPATH,
                             '//android.webkit.WebView[@text="Каталог модной женской одежды, обуви и аксессуаров - интернет-магазин «Befree»"]/android.view.View/android.view.View/android.view.View[3]/android.view.View[5]')).click()

    def auth(self):
        with allure.step("Вставляем email"):
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText')).send_keys(
                self.email)
        with allure.step("Вставляем пароль"):
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')).send_keys(
                self.password)
        with allure.step("Нажимаем 'продолжить'"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="продолжить"]')).click()
        time.sleep(3)

    def check_profile(self):
        self.open_page()
        with allure.step("Отображаетмся Имя Фамилия пользователя"):
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView[2]')).should(
                have.text('Алик Галлямов'))
