import requests

import pytest
from common.allure_ import allure_title
from config.case import case_assert_result
from common.yaml_util import YamlReader


# from config.case import case_assert_result
@pytest.mark.parametrize('case_data', YamlReader().read_case('data.yaml'))
def test_main(case_data: dict):
    # if 'extract_key' in case_data:
    #     print(case_data['extract_key'])
    print(case_assert_result(case_data))
    # print(case_data['assert_expression'])
    # re=requests.post(url=case_data['request']['url'],
    #                                         data=case_data['request']['data'],params=case_data['request']['Params'])
    # print(re.json())
