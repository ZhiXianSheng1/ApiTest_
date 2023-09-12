import pytest

from common.code.case import Case_result
from common.request_common.Requests_util import Request
from common.yaml_common.yaml_util import YamlReader
from conftest import param_pool


class pas:
    @pytest.mark.parametrize('case_data1', YamlReader().read_case('test.yaml'))
    def get_token1(case_data1):
        print(Case_result.cassert_main(case_data=case_data1))
        # mobile = param_pool.parameters['testcase_pool']['mobile']
        # ver_code = param_pool.parameters['testcase_pool']['ver_code']
        # re = Request.requests_api(method="post",
        #                           url='https://demo-api.apipost.cn/api/demo/login',
        #                           data={  # 定义请求数据
        #                               'mobile': mobile,
        #                               'ver_code': ver_code
        #                           }
        #                           )
        # token_value = re["body"]["data"]["token"]
        # return token_value


if __name__ == '__main__':
    print(pas().get_token1())
