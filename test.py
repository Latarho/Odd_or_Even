import requests
import pytest


class TestGetEven():
    """Класс для тестов проверки метода check_even_number."""
    BASE_URI = "http://127.0.0.1:8000/even"

    @pytest.mark.parametrize("number", [0, 2, 22, 222])
    def test_get_check_even_number_positive_even(self, number):
        param_request = {"number": number}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 200
        assert response.json()["result"] == "true"

    @pytest.mark.parametrize("number", [3, 33, 333, 3333])
    def test_get_check_even_number_positive_odd(self, number):
        param_request = {"number": number}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 200
        assert response.json()["result"] == "false"

    @pytest.mark.parametrize("string", ["this is string", {dict: dict}, (tuple, tuple), 1.245])
    def test_get_check_even_number_negative(self, string):
        param_request = {"number": string}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 422
        response_body = response.json()["detail"]
        assert response_body[0]["msg"] == "value is not a valid integer"


class TestGetOdd():
    """Класс для тестов проверки метода check_odd_number."""
    BASE_URI = "http://127.0.0.1:8000/odd"

    @pytest.mark.parametrize("number", [5, 55, 555, 5555])
    def test_get_check_odd_number_positive_odd(self, number):
        param_request = {"number": number}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 200
        assert response.json()['result'] == "true"

    @pytest.mark.parametrize("number", [0, 8, 88, 888])
    def test_get_check_odd_number_positive_even(self, number):
        param_request = {"number": number}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 200
        assert response.json()['result'] == "false"

    @pytest.mark.parametrize("string", ["this is string", {dict: dict}, (tuple, tuple), 5.2355])
    def test_get_check_odd_number_negative(self, string):
        param_request = {"number": string}
        response = requests.get(self.BASE_URI, params=param_request)
        assert response.status_code == 422
        response_body = response.json()["detail"]
        assert response_body[0]["msg"] == "value is not a valid integer"


class TestPostEven():
    """Класс для тестов проверки метода check_even_list."""
    BASE_URI = "http://127.0.0.1:8000/even"

    @pytest.mark.parametrize("list_numbers, expected", [([1, 2, 3, 4, 5, 6], [2, 4, 6]), ([0, 2, 5, 23, 81], [0, 2])])
    def test_post_check_even_list_positive(self, list_numbers, expected):
        response = requests.post(self.BASE_URI, json=list_numbers)
        assert response.status_code == 200
        assert response.json()['result'] == expected

    def test_post_check_even_list_negative(self, list_numbers="This is string"):
        response = requests.post(self.BASE_URI, json=list_numbers)
        assert response.status_code == 422
        response_body = response.json()["detail"]
        assert response_body[0]["msg"] == "value is not a valid list"


class TestPostOdd():
    """Класс для тестов проверки метода check_odd_list."""
    BASE_URI = "http://127.0.0.1:8000/odd"

    @pytest.mark.parametrize("list_numbers, expected", [([1, 2, 3, 4, 5, 6], [1, 3, 5]), ([2, 5, 23, 81], [5, 23, 81])])
    def test_post_check_odd_list_positive(self, list_numbers, expected):
        response = requests.post(self.BASE_URI, json=list_numbers)
        assert response.status_code == 200
        assert response.json()['result'] == expected

    def test_post_check_odd_list_negative(self, list_numbers="This is string"):
        response = requests.post(self.BASE_URI, json=list_numbers)
        assert response.status_code == 422
        response_body = response.json()["detail"]
        assert response_body[0]["msg"] == "value is not a valid list"
