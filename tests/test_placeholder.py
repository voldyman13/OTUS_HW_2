import requests
import pytest
import json
from json import JSONDecodeError

from src.validate_json import validate_json


def test_get_data_of_resource():
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Getting data of resource and response schema validation test
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    res = requests.get(url=url, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, "resource_schema.json")
    assert validation, error


def test_create_resource():
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Resource creation and response schema validation test
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    body = {
        "title": 'Resource creation with POST request',
        "body": 'Resource creation and response schema validation test',
        "userId": 1,
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    res = requests.post(url=url, headers=headers, json=body, verify=False)
    status_code = res.status_code
    assert status_code == 201, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. POST:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, "resource_schema.json")
    assert validation, error


def test_update_resource_with_put():
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Resource updating and response schema validation test
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    body = {
        "id": 1,
        "title": 'Updating a resource with PUT request',
        "body": 'Resource updating and response schema validation test',
        "userId": 1,
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    res = requests.put(url=url, headers=headers, json=body, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. PUT:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, "resource_schema.json")
    assert validation, error


def test_update_resource_with_patch():
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Resource updating and response schema validation test
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    body = {
        "title": 'Updating a resource with PATCH request',
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    res = requests.patch(url=url, headers=headers, json=body, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. PATCH:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, "resource_schema.json")
    assert validation, error


def test_remove_resource():
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Remove data of resource
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    res = requests.delete(url=url, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"


@pytest.mark.parametrize("user_id", [1, 15, 76])
def test_filtering_resources(user_id):
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Status code and schema validation of routs
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"userId": user_id}
    res = requests.get(url=url, params=payload, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, "posts_schema.json")
    assert validation, error


@pytest.mark.parametrize(
    "rout_url, schema", [
        ("https://jsonplaceholder.typicode.com/posts/1/comments", "comments_schema.json"),
        ("https://jsonplaceholder.typicode.com/albums/1/photos", "photos_schema.json"),
        ("https://jsonplaceholder.typicode.com/users/1/albums", "albums_schema.json"),
        ("https://jsonplaceholder.typicode.com/users/1/todos", "todos_schema.json"),
        ("https://jsonplaceholder.typicode.com/users/1/posts", "posts_schema.json")
    ]
)
def test_listing_nested_resources(rout_url, schema):
    """
    Тестирование REST сервиса: "https://jsonplaceholder.typicode.com"
    Status code and schema validation of routs
    """
    res = requests.get(url=rout_url, verify=False)
    status_code = res.status_code
    assert status_code == 200, f"Status code:{status_code}, res.text: {res.text}"
    try:
        json_data = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    validation, error = validate_json(json_data, schema)
    assert validation, error




