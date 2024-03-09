from jsonschema import validate

from befree_tests.api.objects_api import ObjectsApi
from befree_tests.helpers.get_schemas import get_json_schemas


def test_auth_with_api():
    objects_api = ObjectsApi()

    response = objects_api.get_auth_response()

    assert response.status_code == 200
    validate(response.json(), get_json_schemas("auth_json_schemas"))
