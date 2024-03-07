from pathlib import Path


def get_path_schemas(schemas_name):
    return str(Path(__file__).parent.parent.joinpath(f'data/schemas/{schemas_name}.json'))
