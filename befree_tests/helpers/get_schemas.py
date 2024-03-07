import json

from befree_tests.contorls.utils import get_path_schemas


def get_json_schemas(schemas_name):
    with open(get_path_schemas(schemas_name)) as schemas:
        schemas = schemas.read()
    return json.loads(schemas)
