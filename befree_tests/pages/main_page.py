from selene import browser, have, command, be

from config import BrowserSettings

COOKIE_NAME = 'token'


class MainPage:
    env_data = BrowserSettings()


    def open_url(self):
        browser.open('/')

    def open_browser_with_cookie(self, response):
        browser.open('/').driver.add_cookie({"name": COOKIE_NAME, "value": response.json()['token']})
        browser.open('/')

    def add_product_to_cart(self, product_variation_id_in_catalog):
        browser.element('[href="/zhenskaya"]').click()
        browser.element('[href*="yng"]').click()

        browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').click()
        browser.all('[view="group"] > button').second.click()
        browser.element('[class*="addCart"]').click()

    def check_cart(self, product_variation_id_in_catalog, item_title):
        browser.element('[state="goToCart"]').click()
        browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').should(
            have.attribute('data-product-title', f'{item_title}'))

    def delete_product_from_cart(self, product_variation_id_in_catalog):
        browser.element('[href="/cart"]').click()
        browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').perform(
            command.js.scroll_into_view)
        browser.element(
            f'[data-product-variation-id="{product_variation_id_in_catalog}"] [class*="close-icon"]').click()
        browser.element('/html/body/div[3]/div/div/div[2]/div/div/button').click()

    def product_is_not_displayed(self, product_variation_id_in_catalog):
        browser.element(f'[data-product-variation-id="{product_variation_id_in_catalog}"]').should(be.not_.visible)

    def find_product(self, value):
        browser.element('[class="sc-5fd868ca-2 hmWPGp"]').click()
        browser.element('[class="digi-search-form__input"]').type(value)

    def check_result_search(self, value):
        browser.element('[class ="digi-product__main"] [href *= "2236004017"]').should(have.text(value))

    def add_to_favorite(self, product_variation_id_in_card):
        browser.element('[href="/zhenskaya"]').click()
        browser.element('[href*="yng"]').click()
        # browser.element(f'[data-product-variation-id="{product_variation_id_in_card}"] [class*="SDQNw"]').perform(
        #     command.js.click)
        browser.element(f'[data-product-variation-id="{product_variation_id_in_card}"] [class="sc-121d609c-2 fstpFb"]').perform(command.js.scroll_into_view)
        browser.element(f'[data-product-variation-id="{product_variation_id_in_card}"] [type="button"]').click()
        browser.element('[href="/favorites"]').click()