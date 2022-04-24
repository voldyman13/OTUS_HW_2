import json

import jsonschema
from jsonschema import validate


def get_schema(filename):
    """This function loads the json schema"""
    with open(f'../files/{filename}', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data, filename):
    """Json Schema Validation"""
    schema = get_schema(filename)
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err
    message = "Given JSON data is Valid"
    return True, message


def save_schema_to_file(schema, filename):
    with open(f"../files/{filename}", "w") as result_file:
        json.dump(schema, result_file, indent=4)
