from selene import browser, have


class FavoritePage:

    def check_favorites(self, product_variation_id_in_card, item_title):
        browser.element('[class*="category-name"]').should(have.text('избранное'))
        browser.element(
            f'[data-product-variation-id="{product_variation_id_in_card}"] [class*="product-title"]').should(
            have.text(item_title))
