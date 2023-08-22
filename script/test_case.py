import pytest
from common.allure_ import allure_title
from config.case import case_assert_result
from common.yaml_util import YamlReader
from config.case import case_assert_result


@pytest.mark.parametrize('case_data', YamlReader().read_case('data.yaml'))
def test_main(case_data: dict):
    if 'extract_key' in case_data:
        print(case_data['extract_key'])
    # case_title =case_data['case_title']
    # allure_title(case_data)
    # print(case_data)
    # assert case_assert_result(case_data)
    case_title = case_data['case_name']
    allure_title(case_title)
    # print(case_data['request']['data'])

    # a=case_assert_result(case_data)
    # print(case_data['assert_expression'])
