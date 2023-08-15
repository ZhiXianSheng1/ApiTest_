import pytest
import requests


@pytest.fixture(scope="function", autouse=True)
def connection_mysql(request):
    print("之前：连接数据库")
    print("之后：连接数据库")


class Test_fuix:
    @pytest.fixture
    def get_login_fixture(self):
        # print(connection_mysql)
        # conf = Configdata()
        url2 = 'https://demo-api.apipost.cn/api/demo/news_list?mobile=18289454846&theme_news=国际新闻&page=1&pageSize=20'
        # token=Configdata.get_conf_token(conf)['token']
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODI4OTQ1NDg0NiIsInZlcl9jb2RlIjoi8J6JgCIsImV4cCI6MTY5MjA0MDI2MiwiaXNzIjoicHJvOTExIn0.7zTIoMqGwN51PUbFEsNKaPlWNFzaFoFqrtc-2Q8WTf8"
        headers1 = {
            'Content-Type': 'application/json',
            'token': token
        }
        re = requests.get(url=url2, headers=headers1)
        yield re

    def test_login(self, get_login_fixture):
        assert get_login_fixture.status_code == 200
        print(get_login_fixture.status_code)


# if __name__ == '__main__':
#     Test_fuix().get_login_fixture()

'''
request 是 pytest的内置fixture
'''

# 测试数据
# test_data = ["mysql", "ridal"]
#
#
# @pytest.fixture(params=test_data)
# def connection_mysql(request):
#     # 获取当前的测试数据
#     user = request.param
#     print("setup前置函数拿着这个账号去注册：%s" % user)
#     result = "success"
#     return user, result
#
#
# def test_register(register_users):
#     user, result = register_users
#     print("在测试用例里面里面获取到当前测试数据：%s" % user)
#     print(result)
#     assert result == "success"
