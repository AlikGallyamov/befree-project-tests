import pytest
from selene import browser
from befree_tests.api.objects_api import ObjectsApi
from befree_tests.contorls import attach
from befree_tests.pages.main_page import MainPage
from config import config_browser, config_mobile
from befree_tests.models.user_item_data import card_blouse, card_jacket, card_bomber_jacket, card_cardigan, \
    card_t_shirt, card_oversize


@pytest.fixture(autouse=False)
def browser_settings():
    config_browser()

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture()
def add_bomber_jacket_to_cart(get_token):
    objects_api = ObjectsApi()

    token = get_token
    objects_api.add_product_to_cart(token, card_bomber_jacket.product_variation_id_in_card)


@pytest.fixture()
def open_browser_with_cookie():
    main_page = MainPage()
    objects_api = ObjectsApi()
    response = objects_api.get_auth_response()
    main_page.open_browser_with_cookie(response)


@pytest.fixture()
def add_cardigan_to_cart(get_token):
    objects_api = ObjectsApi()

    token = get_token
    objects_api.add_product_to_cart(token, card_cardigan.product_variation_id_in_card)


@pytest.fixture()
def post_remove_blouze_from_cart(get_token):
    objects_api = ObjectsApi()
    token = get_token
    objects_api.remove_item_from_cart(token, card_blouse.product_variation_id_in_catalog)


@pytest.fixture()
def post_remove_jacket_from_cart(get_token):
    objects_api = ObjectsApi()
    token = get_token
    objects_api.remove_item_from_cart(token, card_jacket.product_variation_id_in_catalog)


@pytest.fixture(scope='session')
def get_token():
    objects_api = ObjectsApi()
    token = objects_api.get_auth_response().json()['token']
    return token


@pytest.fixture(autouse=False, scope='session')
def get_favorite_uuid(get_token):
    token = get_token
    objects_api = ObjectsApi()
    uuid = objects_api.generate_favorite_uuid(token).json()['data']['uuid']
    return uuid


@pytest.fixture()
def delete_favorite(get_token, get_favorite_uuid):
    token = get_token
    uuid = get_favorite_uuid
    object_api = ObjectsApi()
    object_api.delete_item_favorite(token, uuid, card_t_shirt.code, card_t_shirt.color_code)


@pytest.fixture()
def delete_favorite_card_oversize(get_token, get_favorite_uuid):
    token = get_token
    uuid = get_favorite_uuid
    object_api = ObjectsApi()
    yield

    object_api.delete_item_favorite(token, uuid, card_oversize.code, card_oversize.color_code)


@pytest.fixture()
def get_cart_id(get_token):
    objects_api = ObjectsApi()
    token = get_token
    cart_id = objects_api.get_cart_info(token).json()['cartId']
    return cart_id

@pytest.fixture
def android_app_manage(context):
    config_mobile(context=context)

    yield
    if context == 'bstack':
        session_id = browser.driver.session_id
        attach.get_video(session_id)
    attach.get_screenshot()
    attach.get_page_source()

    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_emulator"
    )


def pytest_configure(config):
    context = config.getoption("--context")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")