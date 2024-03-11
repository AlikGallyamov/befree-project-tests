from pathlib import Path


def get_path_schemas(schemas_name):
    return str(Path(__file__).parent.parent.joinpath(f'data/schemas/{schemas_name}.json'))


def get_local_path_app():
    return str(Path(__file__).parent.parent.joinpath("source/befree-8-3-1.apk"))


def get_project_path():
    return str(Path(__file__).parent.parent.parent.joinpath(""))

