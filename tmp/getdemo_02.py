from common.request_common.Requests_util import Request

import os

from conftest import param_pool


def get_token1():
    mobile = param_pool.parameters['testcase_pool']['mobile']
    ver_code = param_pool.parameters['testcase_pool']['ver_code']
    re = Request.requests_api(method="post",
                              url='https://demo-api.apipost.cn/api/demo/login',
                              data={  # 定义请求数据
                                  'mobile': mobile,
                                  'ver_code': ver_code
                              }
                              )
    token_value = re["body"]["data"]["token"]
    return token_value


if __name__ == '__main__':
    print(get_token1())
