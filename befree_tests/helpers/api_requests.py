import allure
import requests
import logging
import json
from allure_commons.types import AttachmentType


def request_api(url, endpoint, methode, **kwargs):
    if methode == "get":
        response = requests.get(url + endpoint, **kwargs)
    if methode == "post":
        response = requests.post(url + endpoint, **kwargs)
    if methode == "delete":
        response = requests.delete(url + endpoint, **kwargs)
    if endpoint != '/rest/V3/login':
        with allure.step(f'{methode} {endpoint}'):
            if methode == 'delete' or methode == 'post':
                body = kwargs['json']
                allure.attach(body=json.dumps(body, indent=4, ensure_ascii=False), name="body request",
                              attachment_type=AttachmentType.JSON, extension="JSON")
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=False), name=''"Response",
                          attachment_type=AttachmentType.JSON, extension='json')
            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)
    return response
