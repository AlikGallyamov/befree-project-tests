def search_json(json_data, key, value):
    result = None
    if isinstance(json_data, dict):
        if key in json_data and json_data[key] == value:
            return json_data['id']
        for k, v in json_data.items():
            result = search_json(v, key, value)
            if result is not None:
                return result
    elif isinstance(json_data, list):
        for item in json_data:
            result = search_json(item, key, value)
            if result is not None:
                return result
    return result

def search_json_value(json_data, key, value):
    result = None
    if isinstance(json_data, dict):
        if key in json_data and json_data[key] == value:
            return json_data[key]
        for k, v in json_data.items():
            result = search_json_value(v, key, value)
            if result is not None:
                return result
    elif isinstance(json_data, list):
        for item in json_data:
            result = search_json_value(item, key, value)
            if result is not None:
                return result
    return result


