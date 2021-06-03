from httpx import post
import random
import string

url_base = 'https://reclameaquichallenge.herokuapp.com/'
endpoint = 'complain'
url = url_base + endpoint


title = "Assimilated well-modulated initiative"
description = "Focused bifurcated open architecture"
locale = "Rāwandūz"
company = "Gabcube"


class TestComplains():
    def test_complain_must_return_400_when_receive_a_post_without_title_param(self):
        request = post(url, data={})
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_and_title_value_is_null(self):
        request = post(url, data={'title': ''})
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_without_description_param(self):
        request = post(url, data={'title': title })
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_and_description_value_is_null(self):
        request = post(url , data={'title': title, 'description': '' })
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_without_locale_param(self):
        request = post(url , data={'title': title, 'description': description })
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_and_locale_value_is_null(self):
        request = post(url , data={'title': title, 'description': description, 'locale': '' })
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_without_company_param(self):
        request = post(url , data={'title': title, 'description': description, 'locale': locale})
        assert request.status_code == 400

    def test_complain_must_return_400_when_receive_a_post_and_company_value_is_null(self):
        request = post(url , data={'title': title, 'description': description, 'locale': locale, 'company': '' })
        assert request.status_code == 400

    def test_complain_must_Return_201_if_all_params_are_correct(self):
        request = post(url , data={'title': title, 'description': description, 'locale': locale, 'company': company })
        assert request.status_code == 201


