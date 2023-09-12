import allure
import pytest
from common.code.case import Case_result
from common.yaml_common.yaml_util import YamlReader


@allure.feature("登录模块")
@allure.story("新闻登录接口")
@allure.title("测试接口请求")
@pytest.mark.parametrize('case_data', YamlReader().read_case('data.yaml'))
def test_main(case_data: dict):
    with allure.step("执行测试用例"):
        print(Case_result.cassert_main(case_data))

    with allure.step("添加断言结果"):
        assert_result = Case_result.cassert_main(case_data)
        if assert_result:
            allure.attach("断言结果", "通过")
        else:
            allure.attach("断言结果", "失败")

    with allure.step("添加请求信息"):
        allure.attach("请求方法", case_data['request']['method'])
        allure.attach("请求URL", case_data['request']['url'])
        allure.attach("请求Headers", str(case_data['request']['headers']))
        allure.attach("请求数据", str(case_data['request']['data']))

    with allure.step("添加提取数据"):
        if 'extract_request' in case_data:
            allure.attach("提取请求数据", str(case_data['extract_request']))
        if 'extract_response' in case_data:
            allure.attach("提取响应数据", str(case_data['extract_response']))

    with allure.step("添加断言表达式"):
        allure.attach("断言表达式", str(case_data['assert_expression']))
