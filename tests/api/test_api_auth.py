import requests
from selene import browser
from jsonschema import validate

from befree_tests.api.objects_api import ObjectsApi
from befree_tests.helpers.get_schemas import get_json_schemas
from befree_tests.pages.main_page import MainPage


def test_auth_with_api():
    objects_api = ObjectsApi()

    response = objects_api.get_auth_response()
    response_json = response.json()

    assert response.status_code == 200
    validate(response_json, get_json_schemas("auth_json_schemas"))


def test_add_product_via_api():
    objects_api = ObjectsApi()

    objects_api.get_auth_response()
    response = objects_api.add_product_to_cart()

    assert response.status_code == 200
