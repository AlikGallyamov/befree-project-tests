import allure
import requests
import logging

import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def post_request(url, methode, **kwargs):
    response = requests.post(url + methode, **kwargs)
    if methode != '/rest/V3/login':
        with step(f"POST{methode}"):
            curl = curlify.to_curl(response.request)
            logging.info(curl)
            allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response


def get_request(url, methode, **kwargs):
    response = requests.get(url + methode, **kwargs)

    return response


def delete_request(url, methode, **kwargs):
    response = requests.delete(url + methode, **kwargs)

    return response
