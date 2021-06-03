from httpx import get

url_base = 'https://reclameaquichallenge.herokuapp.com/'
endpoint = 'countcomplains'
url = url_base + endpoint

locale = "Rāwandūz"
company = "Gabcube"

class TestTask():
    def test_count_complains_must_return_400_when_receive_a_get_without_code_param(self):
        request = get(url, params={})
        assert request.status_code == 400

    def test_count_complains_must_return_400_when_receive_a_get_with_empty_title(self):
        request = get(url, params={'company': company})
        assert request.status_code == 400

    def test_count_complains_must_return_400_when_receive_a_get_with_empty_company(self):
        request = get(url, params={'locale': locale})
        assert request.status_code == 400

    def test_count_complains_must_return_200_when_receive_a_get_with_all_params(self):
        request = get(url, params={'locale': locale, 'company': company})
        assert request.status_code == 200
