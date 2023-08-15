import requests

from common.yaml_util import read_yaml
url2 = 'https://demo-api.apipost.cn/api/demo/news_list?mobile=18289454846&theme_news=国际新闻&page=1&pageSize=20'
headers1 = {
    'Content-Type': 'application/json',
    'token': read_yaml("token")
}
re = requests.get(url=url2,headers=headers1)
res = re.json()
print(res)
# articl = res['data']['lists']
# for articl_data in articl:
#     print(articl_data['id'])
#     print(articl_data['title'])
#     print(articl_data['content'])
# assert res['code'] == 10000
import pytest
# print(pytest.__version__)