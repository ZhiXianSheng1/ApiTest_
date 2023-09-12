from common.assert_common.Case_assert_result import Assert_judge
from common.code.Case_Api_response import Api_response
from common.code.extract_data import Extract_dataProcess

"""
    功能执行页，如request请求获取、断言结果

"""


class Case_result:
    @classmethod
    def cassert_main(cls, case_data):
        Extract_dataProcess.extract_request_response(case_data, Api_response.casedata_api_response(case_data))
        Assert_judge.assert_judge(case_data, Api_response.casedata_api_response(case_data))
