import pytest
import requests
import json
from common.yaml_util import clean_yaml, write_yaml, read_yaml


#在所有的接口请求之前执行
# @pytest.fixture(scope="session",autouse=True)#自动执行
# def clean_extract():
#     print("清理数据")
#     clean_yaml()

@pytest.fixture
def login():
    url = 'https://demo-api.apipost.cn/api/demo/login'
    payload = {  # 定义请求数据
        'mobile': '18289454846',
        'ver_code': '123456'
    }
    # headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(payload)  # 转换为json格式
    # 发送POST请求
    response = requests.post(url=url, data=payload)
    result = response.json()

    write_yaml({"token": result['data']['token']})
    token = read_yaml("token")
    yield token


