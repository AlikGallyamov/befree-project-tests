from pathlib import Path

import requests


def get_path_schemas(schemas_name):
    return str(Path(__file__).parent.parent.joinpath(f'data/schemas/{schemas_name}.json'))


def get_local_path_app():
    return str(Path(__file__).parent.parent.joinpath("source/befree-8-3-1.apk"))


def get_url_app(user_name, access_key, cloud_url):
    test_file = open(get_local_path_app(), "rb")
    response = requests.post(cloud_url, auth=(user_name, access_key),
                             files={"file": test_file})
    return response.json()["app_url"]


user_name = "azgallyamov_0wTr3j"
access_key = "mckBkK9h5XxxhVcXBnpq"
cloud_url = "https://api-cloud.browserstack.com/app-automate/upload"
print(get_url_app(user_name, access_key, cloud_url))