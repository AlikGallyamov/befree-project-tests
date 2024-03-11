import allure
from jsonschema import validate

from befree_tests.api.objects_api import ObjectsApi
from befree_tests.helpers.get_schemas import get_json_schemas
from befree_tests.data.user_item_data import card_oversize, card_dress


def test_add_to_favorite(get_token, get_favorite_uuid, delete_favorite_card_oversize):
    token = get_token
    uuid = get_favorite_uuid
    objects_api = ObjectsApi()

    response = objects_api.add_item_to_favorite(token, uuid, card_oversize.code, card_oversize.color_code)

    with allure.step('Проверяем статус'):
        assert response.status_code == 200
    with allure.step('Проверяем соответствие json схеме'):
        validate(response.json(), get_json_schemas("add_product_to_favorite"))
    with allure.step('Проверяем, что товар добавился в избранное'):
        assert objects_api.item_in_favorite(response.json(), card_oversize.code) == card_oversize.code


def test_favorite_info(get_token, get_favorite_uuid, delete_favorite_card_oversize):
    token = get_token
    uuid = get_favorite_uuid
    objects_api = ObjectsApi()

    response = objects_api.get_favorite_items(token, uuid)

    with allure.step('Проверяем статус'):
        assert response.status_code == 200
    with allure.step('Проверяем, что в избранном есть товар'):
        assert objects_api.item_in_favorite(response.json(), card_dress.code) == card_dress.code
    with allure.step('Проверяем соответствие json схеме'):
        validate(response.json(), get_json_schemas("info_favorite_schemas"))
