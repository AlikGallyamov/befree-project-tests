from befree_tests.api.objects_api import ObjectsApi
from befree_tests.pages.main_page import MainPage


def test_add_to_cart(browser_settings):
    main_page = MainPage()
    objects_api = ObjectsApi()
    response = objects_api.get_auth_response()
    main_page.open_browser_with_cookie(response)
