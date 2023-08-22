import pytest
import requests
import json

from jsonpath import jsonpath

from common.Requests_util import Request
from common.yaml_util import YamlReader

# @pytest.mark.parametrize('case_data',YamlReader().read_case('data.yaml'))
# def test_a(case_data):
#     api_response = Request.requests_api(method=case_data['request']['method'], url=case_data['request']['url'],
#                                         data=case_data['request']['data'])
#     print(api_response)
#     a=jsonpath(api_response,'$.body.code')
#     a=a[0]
#     print(a)
api_response = {'status_code': 200, 'body': {'code': 10000, 'data': {
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODI4OTQ1NDg0NiIsInZlcl9jb2RlIjoi8J6JgCIsImV4cCI6MTY5MjU4ODE1NCwiaXNzIjoicHJvOTExIn0.PZfF7FoCXojjd4nRQZEAuFZWhFj1HpLmvPntGCFW8mc'},
                                             'msg': 'success'}}
# assert_list = ["'12' in '123'", "'ig' == '$.ig'",'2 == 1']
# api_response = {'msg': '请求正常','ig': 'theshy'}
assert_list = ['status_code == $.status_code', 'code == $.body.code', 'token == $.body.data.token']
i = "'msg' == '$.body.msg'"
if '$.' in i:
    wz = i.find('$')
    print(wz)
    assert_json_path = i[wz:len(i) - 1]
    print(assert_json_path)
    # c = assert_json_path
    value = jsonpath(api_response, "$.body")
    print(value)

assert_list1 = ["'status_code' == '$.status_code'", "'msg' == '$.body.msg'", 'token == $.body.data.token']
print(assert_list1[0])
