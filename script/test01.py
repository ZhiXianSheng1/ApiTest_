import pytest
import requests
import json

from common.yaml_util import write_yaml, read_yaml


class Test_pytest():
    def test_token(self,login):
        url2 = 'https://demo-api.apipost.cn/api/demo/news_list?mobile=18289454846&theme_news=国际新闻&page=1&pageSize=20'
        headers1 = {
            'Content-Type': 'application/json',
            'token': login
        }
        re = requests.get(url=url2, headers=headers1)
        res = re.json()
        print(res)

        # pass

    def test_02(self):
        print("this is test02")





