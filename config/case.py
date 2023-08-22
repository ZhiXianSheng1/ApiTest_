from common.Assert_util import Assert

from common.ParameterSetting import ParameterSetting
from common.Requests_util import Request


def extract_(api_response, extract_key):
    if extract_key:
        extract_value = ParameterSetting.extract_value(api_response, extract_key)
        ParameterSetting.parameter_setting(extract_value, 'save')


def case_assert_result(case_data):
    if case_data['request']['method'] == 'get':
        api_response = Request.requests_api(method=case_data['request']['method'], url=case_data['request']['url'],
                                            data=case_data['request']['data'])
        if 'extract_key' in case_data:
            extract_key = case_data['extract_key']
            extract_(api_response, extract_key)
        assert_r = Assert.assert_resonse(api_response, case_data["assert_expression"])
        return assert_r

    elif case_data['request']['method'] == 'post':
        if ParameterSetting.data_is_replace(case_data['request']['data']):
            data = ParameterSetting.parameter_setting(case_data['data'], 'get')
        data = case_data['request']['data']
        api_response = Request.requests_api(method=case_data['request']['method'], url=case_data['request']['url'],
                                            data=data)
        if 'extract_key' in case_data:
            extract_key = case_data['extract_key']
            extract_(api_response, extract_key)
        assert_r = Assert.assert_resonse(api_response, case_data["assert_expression"])
        # print(access_value)
        return assert_r
        pass
