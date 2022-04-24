import requests
import validators
import pytest
import json
from json import JSONDecodeError


@pytest.mark.parametrize("code, url", [
                            (200, "https://dog.ceo/api/breeds/list/"),
                            (200, "https://dog.ceo/api/breeds/list/all"),
                            (200, "https://dog.ceo/api/breeds/image/random")])
def test_check_status_code(code, url):
    """
    Тестирование REST сервиса: https://dog.ceo
    Checking of status code of services
    """
    res = requests.get(url=url, verify=False)
    assert res.status_code == code, "Код ответа не соответствует"


def test_check_header():
    """
    Тестирование REST сервиса: https://dog.ceo
    Header Check Example (Content-Type)
    """
    url = "https://dog.ceo/api/breeds/list/"
    res = requests.get(url=url, verify=False)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json', "Expected 'Content-Type' is 'application/json'"


def test_check_breeds_list():
    """
    Тестирование REST сервиса: https://dog.ceo
    Checking dog breeds list
    """
    url = "https://dog.ceo/api/breeds/list/"
    res = requests.get(url=url, verify=False)
    assert res.status_code == 200
    try:
        response = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. {res.text}"
    breeds = response['message']
    assert isinstance(breeds, list) and len(breeds) > 0


@pytest.mark.parametrize("breed", ["boxer", "bulldog", "bullterrier"]
                         )
def test_find_breed_in_list(breed):
    """
    Тестирование REST сервиса: https://dog.ceo
    Find breed in list
    """
    url = "https://dog.ceo/api/breeds/list/"
    res = requests.get(url=url, verify=False)
    assert res.status_code == 200
    try:
        response = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    breeds = response["message"]
    assert breed in breeds


def test_validate_image_url():
    """
    Тестирование REST сервиса: https://dog.ceo
    validation of image url
    """
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url=url, verify=False)
    assert res.status_code == 200
    try:
        response = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    image = response["message"]
    # валидация линка
    assert validators.url(image)


def test_check_image_link():
    """
    Тестирование REST сервиса: https://dog.ceo
    checking image link
    """
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url=url, verify=False)
    assert res.status_code == 200
    try:
        response = json.loads(res.text)
    except JSONDecodeError:
        assert False, f"Can't parse the response. GET:{res.url}\nResponse: {res.text}"
    image_url = response["message"]
    # проверяем ссылку на имидж
    res = requests.get(image_url)
    assert 200 == res.status_code
    path = "../files/img.jpg"
    # сохраняем имидж в файл
    with open(path, "wb") as out:
        out.write(res.content)
    # определяем формат файла
    import imghdr
    assert imghdr.what(path) in ["jpeg", "png"]
    # удаляем файл
    import os
    os.remove(path)
