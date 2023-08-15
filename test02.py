import requests

url = 'https://demo-api.apipost.cn/api/demo/login'

# 定义请求数据
payload = {
    'mobile': '18289454846',
    'ver_code': '123456'
}
# 发送POST请求
response = requests.post(url=url, data=payload)
result = response.json()
token =
print(result)
assert result['code'] == 10000
assert 'token' in result['data']
assert result['msg'] == 'success'