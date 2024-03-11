from befree_tests.data.user_item_data import card_t_shirt
from befree_tests.pages.favorites_page import FavoritePage
from befree_tests.pages.main_page import MainPage


def test_add_to_favorite(browser_settings, delete_favorite, open_browser_with_cookie):
    main_page = MainPage()
    favorite_page = FavoritePage()
    main_page.add_to_favorite(card_t_shirt.product_variation_id_in_catalog)
    favorite_page.check_favorites(card_t_shirt.product_variation_id_in_card, card_t_shirt.item_title)
