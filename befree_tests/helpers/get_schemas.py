import json
from pathlib import Path
from befree_tests.contorls.utils import get_project_path


def get_json_schemas(schemas_name):
    scchemas_path = Path(get_project_path(), "befree_tests", "data", "schemas", f"{schemas_name}.json")
    with open(scchemas_path) as schemas:
        schemas = schemas.read()
    return json.loads(schemas)
