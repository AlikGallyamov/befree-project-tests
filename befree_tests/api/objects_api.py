import os

import allure

from dotenv import load_dotenv

from befree_tests.contorls.utils import get_project_path
from befree_tests.data.json_body.request_body import auth_body, add_product_body, headers_auth, \
    delete_item_from_cart_body, favorites
from befree_tests.helpers.api_requests import request_api
from befree_tests.helpers.find_element_to_json import search_json, search_json_value


class ObjectsApi:
    def __init__(self):
        load_dotenv(get_project_path() + '/.env')
        load_dotenv(get_project_path() + '/.env.stage')
        self.password = os.getenv('password')
        self.base_url = os.getenv('base_url')
        self.back_url = os.getenv('back_url')
        self.catalog_url = os.getenv('catalog_url')
        self.email = os.getenv('email')

    @allure.step('Запрашиваем данные авторизации')
    def get_auth_response(self):
        endpoint = '/rest/V3/login'
        methode = 'post'
        data = auth_body
        data['email'] = self.email
        data['password'] = self.password

        response = request_api(self.back_url, endpoint, methode, json=data)
        return response

    @allure.step('Добавляем товар в корзину по АПИ')
    def add_product_to_cart(self, token, product_variation_id_in_card):
        data = add_product_body
        data['product'] = product_variation_id_in_card
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        endpoint = '/rest/V3/cart'
        methode = 'post'
        response = request_api(self.back_url, endpoint, methode, headers=headers, json=data)
        return response

    @allure.step('Запрашиваем информацию о корзине')
    def get_cart_info(self, token):
        endpoint = '/rest/V3/customer?full=1&with=level'
        methode = 'get'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = request_api(self.back_url, endpoint, methode, headers=headers)

        return response

    @allure.step('Запрашиваем информацию по товару')
    def get_items_info_from_cart(self, token, cart_id):
        endpoint = '/rest/V3/cart/'
        methode = 'get'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token

        endpoint = endpoint + cart_id

        response = request_api(self.back_url, endpoint, methode, headers=headers)
        return response

    @allure.step('Удаляем товар из корзины по АПИ')
    def remove_item_from_cart(self, token, product_variation_id_in_catalog):
        cart_id = self.get_cart_info(token).json()['cartId']
        items_info = self.get_items_info_from_cart(token, cart_id).json()
        endpoint = '/rest/V3/cart/' + cart_id
        methode = 'delete'
        item_id = search_json(items_info, 'product_variation_id', product_variation_id_in_catalog)
        data = delete_item_from_cart_body
        data['itemIds'].append(item_id)

        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = request_api(self.back_url, endpoint, methode, headers=headers, json=data)

        return response

    def item_in_cart(self, token, product_variation_id_in_card):
        cart_id = self.get_cart_info(token).json()['cartId']
        items_info = self.get_items_info_from_cart(token, cart_id).json()
        return search_json(items_info, 'product_variation_id', product_variation_id_in_card)

    @allure.step('Генерируем UUID')
    def generate_favorite_uuid(self, token):
        endpoint = '/public/v2/favorites'
        methode = 'get'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = request_api(self.catalog_url, endpoint, methode, headers=headers)
        return response

    @allure.step('Удаляем товар из избранного по АПИ')
    def delete_item_favorite(self, token, uuid, article, color_code):
        endpoint = '/public/v2/favorites/' + uuid
        methode = 'delete'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        data = favorites
        data['article'] = article
        data['color_code'] = color_code
        request_api(self.catalog_url, endpoint, methode, headers=headers, json=data)

    @allure.step('Запрашиваем содержимое избранного')
    def get_favorite_items(self, token, uuid):
        endpoint = '/public/v2/favorites/' + uuid
        methode = 'get'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = request_api(self.catalog_url, endpoint, methode, headers=headers)
        return response

    @allure.step('Добавляем товар в избранное по АПИ')
    def add_item_to_favorite(self, token, uuid, article, color_code):
        endpoint = '/public/v2/favorites/' + uuid
        methode = 'post'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        data = favorites
        data['article'] = article
        data['color_code'] = color_code
        return request_api(self.catalog_url, endpoint, methode, headers=headers, json=data)

    def item_in_favorite(self, data, article):
        return search_json_value(data, 'article', article)
