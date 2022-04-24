import requests


def test_status_code_check(url, code):
    """ run example: pytest ../tests/test_status_code_check.py --url=https://mail.ru --status_code=200 """
    response = requests.get(url=url, )
    assert response.status_code == code, "Код ответа не соответствует"
