import allure
import requests
import logging

import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def request_api(url, endpoint, methode, **kwargs):
    if methode == "get":
        response = requests.get(url + endpoint, **kwargs)
    if methode == "post":
        response = requests.post(url + endpoint, **kwargs)
    if methode == "delete":
        response = requests.delete(url + endpoint, **kwargs)
    if endpoint != '/rest/V3/login':
        with step(f"POST{endpoint}"):
            curl = curlify.to_curl(response.request)
            logging.info(curl)
            allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
