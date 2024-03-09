from befree_tests.data.json_body.request_body import auth_body, add_product_body, headers_auth, \
    delete_item_from_cart_body, favorites
from befree_tests.helpers.api_requests import post_request, get_request, delete_request
from befree_tests.helpers.find_element_to_json import search_json, search_json_value

from config import BrowserSettings


class ObjectsApi:
    env_data = BrowserSettings()

    def get_auth_response(self):
        method = '/rest/V3/login'
        data = auth_body
        data['email'] = self.env_data.email
        data['password'] = self.env_data.password

        response = post_request(self.env_data.back_url, method, json=data)
        print(response)
        return response

    def add_product_to_cart(self, token, product_variation_id_in_card):
        data = add_product_body
        data['product'] = product_variation_id_in_card
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        method = '/rest/V3/cart'
        response = post_request(self.env_data.back_url, method, headers=headers, json=data)
        return response

    def get_cart_info(self, token):
        methode = '/rest/V3/customer?full=1&with=level'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = get_request(self.env_data.back_url, methode, headers=headers)

        return response

    def get_items_info_from_cart(self, token, cart_id):
        methode = '/rest/V3/cart/'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token

        methode = methode + cart_id

        response = get_request(self.env_data.back_url, methode, headers=headers)
        return response

    def remove_item_from_cart(self, token, product_variation_id_in_catalog):
        cart_id = self.get_cart_info(token).json()['cartId']
        items_info = self.get_items_info_from_cart(token, cart_id).json()
        methode = '/rest/V3/cart/'
        item_id = search_json(items_info, 'product_variation_id', product_variation_id_in_catalog)
        data = delete_item_from_cart_body
        data['itemIds'].append(item_id)

        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = delete_request(self.env_data.back_url, methode + cart_id, headers=headers, json=data)

        return response

    def item_in_cart(self, token, product_variation_id_in_card):
        cart_id = self.get_cart_info(token).json()['cartId']
        items_info = self.get_items_info_from_cart(token, cart_id).json()
        return search_json(items_info, 'product_variation_id', product_variation_id_in_card)

    def generate_favorite_uuid(self, token):
        methode = '/public/v2/favorites'
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = get_request(self.env_data.catalog_url, methode, headers=headers)
        return response

    def delete_item_favorite(self, token, uuid, article, color_code):
        methode = '/public/v2/favorites/' + uuid
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        data = favorites
        data['article'] = article
        data['color_code'] = color_code
        delete_request(self.env_data.catalog_url, methode, headers=headers, json=data)

    def get_favorite_items(self, token, uuid):
        methode = '/public/v2/favorites/' + uuid
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        response = get_request(self.env_data.catalog_url, methode, headers=headers)
        return response

    def add_item_to_favorite(self, token, uuid, article, color_code):
        methode = '/public/v2/favorites/' + uuid
        headers = headers_auth
        headers['Authorization'] = 'Bearer ' + token
        data = favorites
        data['article'] = article
        data['color_code'] = color_code
        return post_request(self.env_data.catalog_url, methode, headers=headers, json=data)

    def item_in_favorite(self, data, article):
        return search_json_value(data, 'article', article)
