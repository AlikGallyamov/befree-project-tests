import allure
import requests
import logging

import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def post_request(url, methode_name, **kwargs):
    response = requests.post(url + methode_name, **kwargs)
    if methode_name != '/rest/V3/login':
        with step(f"POST{methode_name}"):
            curl = curlify.to_curl(response.request)
            logging.info(curl)
            allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
