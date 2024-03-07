from befree_tests.data.json_body.request_body import auth_body, add_product_body
from befree_tests.helpers.api_requests import post_request
from config import BrowserSettings


class ObjectsApi():
    env_data = BrowserSettings()

    def get_auth_response(self):
        method = '/rest/V3/login'
        data = auth_body
        data['email'] = self.env_data.email
        data['password'] = self.env_data.password

        response = post_request(self.env_data.back_url, method, json=data)
        return response

    def add_product_to_cart(self):
        method = '/rest/V3/cart'
        data = add_product_body

        response = post_request(self.env_data.back_url, method, json=data)
        return response
