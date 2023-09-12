from common.log_common.log_util import Logger
from common.code.ParameterSetting import ParameterSetting
from conftest import param_pool

"""$. 参数处理类"""


class Extract_dataProcess:
    @classmethod
    def extract_request_response(cls, case_data, api_response):
        """
        :param api_response:处理要获取api请求里字段带$
        :param response_data:
        :return:
        """
        if 'extract_response' in case_data:
            response_data = case_data['extract_response']
            Logger.my_log().info(f'需要处理的值response_data为{response_data}')
            extract_value = ParameterSetting.extract_value(api_response=api_response, extract_response=response_data)
            Logger.my_log().info(f"需要处理的值extract_response为{extract_value}")
            data_result = ParameterSetting.parameter_setting(extract_value, 'save')
            Logger.my_log().info(f"数据extract_response为{data_result}")
            return data_result
        if 'extract_request' in case_data:
            request_data = case_data['extract_request']
            Logger.my_log().info(f'需要处理的值extract_request为{request_data}')
            extract_value = ParameterSetting.extract_value(case_data=case_data, extract_request=request_data)
            Logger.my_log().info(f"需要处理的值extract_request为{extract_value}")
            data_result = ParameterSetting.parameter_setting(extract_value, 'save')
            Logger.my_log().info(f"数据extract_request为{data_result}")
            return data_result

    @classmethod
    def extract_data(cls, case_data):
        response_data = case_data['request']['data']
        Logger.my_log().info(f"response_data的值存在{response_data}")
        extract_datavalue = ParameterSetting.extract_value(case_data=param_pool.parameters,
                                                           extract_request=response_data)
        Logger.my_log().info(f"数据extract_datavalue的值存在{extract_datavalue}")
        return extract_datavalue
