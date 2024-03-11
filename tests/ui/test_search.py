from befree_tests.data.user_item_data import card_for_find
from befree_tests.pages.main_page import main_page


def test_find_product_code(browser_settings, open_browser_with_cookie):
    main_page.find_product(card_for_find.code)
    main_page.check_result_search(card_for_find.item_title)


def test_find_product_name(browser_settings, open_browser_with_cookie):
    main_page.find_product(card_for_find.item_title)
    main_page.check_result_search(card_for_find.item_title)
