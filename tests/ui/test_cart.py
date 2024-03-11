from befree_tests.data.user_item_data import card_blouse, card_cardigan
from befree_tests.pages.main_page import MainPage


def test_add_to_cart(browser_settings, post_remove_blouze_from_cart, open_browser_with_cookie, ):
    main_page = MainPage()

    main_page.add_product_to_cart(card_blouse.product_variation_id_in_card)

    main_page.check_cart(card_blouse.item_title)


def test_delete_product_from_cart(browser_settings, add_cardigan_to_cart, open_browser_with_cookie):
    main_page = MainPage()
    main_page.delete_product_from_cart(card_cardigan.product_variation_id_in_catalog)
    main_page.product_is_not_displayed(card_cardigan.product_variation_id_in_catalog)
