from common.code.ParameterSetting import ParameterSetting
from common.code.extract_data import Extract_dataProcess
from common.log_common.log_util import Logger
from common.request_common.Requests_util import Request

"""api 的api_response字段值获取"""


class Api_response:
    @classmethod
    def casedata_api_response(cls, case_data):
        # 验证case_data是否包含所需的键
        if not all(key in case_data['request'] for key in ['method', 'url', 'data']):
            Logger.my_log(log_level='ERROR').error('case_data缺失相应得健')
            raise ValueError("case_data缺失相应得健")

        if case_data['request']['method'] == 'get':
            api_response = Request.get(url=case_data['request']['url'],
                                       data=case_data['request']['data'])
            return api_response

        elif case_data['request']['method'] == 'post':
            if ParameterSetting.data_is_replace(case_data['request']['data']):
                data = Extract_dataProcess.extract_data(case_data)
            else:
                data = case_data['request']['data']
            api_response = Request.post(url=case_data['request']['url'],
                                        data=data)
            return api_response
        else:
            Logger.my_log(log_level='ERROR').error('request method不存在')
            raise ValueError("request method不存在")
