import allure
from dotenv import load_dotenv
from selene import browser, have, command, be

from befree_tests.data.cookie_auth import location

COOKIE_NAME = 'token'
COOKIE_LOCATION = 'location'


class MainPage:
    env_data = load_dotenv('.env')

    def open_url(self):
        with allure.step("Открываем браузер"):
            browser.open('/')

    def open_browser_with_cookie(self, response):
        with allure.step("Загружаем куки в сессию"):
            browser.open('/').driver.add_cookie({
                "name": COOKIE_NAME, "value": response.json()['token']
            })
        browser.open('/').driver.add_cookie({
            "name": COOKIE_LOCATION, "value": location
        })
        browser.open('/')
        try:
            with allure.step("Принимаем куки на интерфейсе"):
                browser.element('[class="sc-7d7c1299-0 hebVCJ button"]').click()
        except Exception:
            return

    def add_product_to_cart(self, product_variation_id_in_card):
        with allure.step("Открыли виджет"):
            browser.element('[href="/zhenskaya"]').click()
        with allure.step("Выбрали категорию"):
            browser.element('[href*="yng"]').click()
        browser.element('[class="sc-db8f3a8e-0 kdUMih"]').perform(command.js.scroll_into_view)
        with allure.step(f"Открыли карточку товара с product-id {product_variation_id_in_card}"):
            browser.element(f'[data-product-variation-id="{product_variation_id_in_card}"]').click()
        with allure.step("Выбрали размер"):
            browser.all('[view="group"] > button').second.click()
        with allure.step("Добавили в корзину"):
            browser.element('[class*="addCart"]').click()

    def check_cart(self, item_title):
        with allure.step("Кликнули 'Перейти в корзину'"):
            browser.element('[state="goToCart"]').click()
        with allure.step(f"Отображается товар с названием {item_title}"):
            browser.element(f'[data-product-title="{item_title}"]').should(be.visible)

    def delete_product_from_cart(self, product_variation_id_in_catalog):
        with allure.step("Клик по корзине"):
            browser.element('[href="/cart"]').click()
        with allure.step("Перешли по вкладке 'Доступно по доставке'"):
            browser.element('[class="sc-792d59e-1 iVTurG"]').click()
        browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').perform(
            command.js.scroll_into_view)
        with allure.step(f"Удаляем товар с product-id {product_variation_id_in_catalog}"):
            browser.element(
                f'[data-product-variation-id="{product_variation_id_in_catalog}"] [class*="close-icon"]').click()
        with allure.step("Подтвердили удаление"):
            browser.element('[class*="eHeVh cPSfug"]').click()

    def product_is_not_displayed(self, product_variation_id_in_catalog):
        with allure.step(f"Товар с product-id {product_variation_id_in_catalog} не отображается"):
            browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').should(be.not_.visible)

    def find_product(self, value):
        with allure.step("Открываем строку поиска"):
            browser.element('[class="sc-5fd868ca-2 hmWPGp"]').click()
        with allure.step(f"Вводим {value}"):
            browser.element('[class="digi-search-form__input"]').type(value)

    def check_result_search(self, value):
        with allure.step(f"Товар {value} отображается"):
            browser.element('[class ="digi-product__main"] [href *= "2236004017"]').should(have.text(value))

    def add_to_favorite(self, product_variation_id_in_card):
        with allure.step("Открываем виджет"):
            browser.element('[href="/zhenskaya"]').click()
        with allure.step("Выбираем категорию"):
            browser.element('[href*="yng"]').click()
        browser.element(
            f'[data-product-variation-id="{product_variation_id_in_card}"] [class="sc-121d609c-2 fstpFb"]').perform(
            command.js.scroll_into_view)
        with allure.step(f"Добавляем товар {product_variation_id_in_card} в избранное"):
            browser.element(f'[data-product-variation-id="{product_variation_id_in_card}"] [type="button"]').click()
        browser.element('[href="/favorites"] [class*="kMteZM"]').should(have.text('1'))
        with allure.step("Перешли в избранное"):
            browser.element('[href="/favorites"]').click()
