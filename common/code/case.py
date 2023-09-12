from common.log_common.log_util import Logger
from common.assert_common.Assert_util import Assert
from common.code.ParameterSetting import ParameterSetting
from common.request_common.Requests_util import Request

"""
    功能执行页，如request请求获取、断言结果

"""


def extract_(api_response, response_data):
    Logger.my_log().info(f"extract_value的值存在{response_data}")
    extract_value = ParameterSetting.extract_value(api_response=api_response, extract_response=response_data)
    ParameterSetting.parameter_setting(extract_value, 'save')


def extract_1(case_data, request_data):
    Logger.my_log().info(f"extract_value的值存在{request_data}")
    extract_value = ParameterSetting.extract_value(case_data=case_data, extract_request=request_data)
    Logger.my_log().info(f"extract_value的值存在{extract_value}")
    ParameterSetting.parameter_setting(extract_value, 'save')


# except TypeError:
#     raise print("参数不存在，请检查")


def case_assert_result(case_data):
    if case_data['request']['method'] == 'get':
        api_response = Request.get(url=case_data['request']['url'],
                                   data=case_data['request']['data'])
        print(api_response)
        if 'extract_response' in case_data:
            response_data = case_data['extract_response']
            Logger.my_log().info(f'extract_key的值为{response_data}')
            a2 = response_data
            extract_(api_response, response_data)
        if 'extract_request' in case_data:
            request_data = case_data['extract_request']
            Logger.my_log().info(f'extract_request的值为{request_data}')
            extract_1(case_data, request_data)
        assert_r = Assert.assert_resonse(api_response, case_data["assert_expression"])
        return assert_r

    elif case_data['request']['method'] == 'post':
        if ParameterSetting.data_is_replace(case_data['request']['data']):
            data = ParameterSetting.parameter_setting(case_data['data'], 'get')
        data = case_data['request']['data']
        api_response = Request.post(url=case_data['request']['url'],
                                    data=data)
        print(api_response)
        Logger.my_log().info(f"response请求为：{api_response}")
        if 'extract_response' in case_data:
            response_data = case_data['extract_response']
            Logger.my_log().info(f'extract_key的值为{response_data}')
            a2 = response_data
            extract_(api_response, response_data)
        if 'extract_request' in case_data:
            request_data = case_data['extract_request']
            Logger.my_log().info(f'extract_request的值为{request_data}')
            extract_1(case_data, request_data)
        # assert_r = Assert.assert_resonse(api_response, case_data["assert_expression"])
        # return assert_r
        pass
