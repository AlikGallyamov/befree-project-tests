import allure
import requests
import logging
import json
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
        # with step(f"{methode}{endpoint}"):
        #     curl = curlify.to_curl(response.request)
        #     logging.info(curlify.to_curl(response.request))
        #     logging.info(response.request.url)
        #     logging.info(response.status_code)
        #     logging.info(response.text)
        #     allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        with allure.step(f'{methode} {endpoint}'):
            curl = curlify.to_curl(response.request)
            allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt", )
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name=''"Response",
                          attachment_type=AttachmentType.JSON, extension='json')
            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)
    return response
