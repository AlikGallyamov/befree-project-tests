from befree_tests.data.user_item_data import card_t_shirt, card_t_shirt_cropped
from befree_tests.pages.main_page import main_page


def test_filter_color(browser_settings, open_browser_with_cookie):
    main_page.set_filter_color()

    main_page.check_color(card_t_shirt_cropped.product_variation_id_in_card, card_t_shirt_cropped.color)


def test_filter_size(browser_settings, open_browser_with_cookie):
    main_page.set_filter_size()

    main_page.check_size(card_t_shirt.product_variation_id_in_catalog)
