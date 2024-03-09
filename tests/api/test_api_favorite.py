from jsonschema import validate

from befree_tests.api.objects_api import ObjectsApi
from befree_tests.helpers.get_schemas import get_json_schemas
from befree_tests.models.user_item_data import card_oversize


def test_add_to_favorite(get_token, get_favorite_uuid, delete_favorite_card_oversize):
    token = get_token
    uuid = get_favorite_uuid
    objects_api = ObjectsApi()

    response = objects_api.add_item_to_favorite(token, uuid, card_oversize.code, card_oversize.color_code)

    assert objects_api.item_in_favorite(response.json(), card_oversize.code) == card_oversize.code
    validate(response.json(), get_json_schemas("add_product_to_favorite"))
    assert response.status_code == 200
