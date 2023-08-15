import allure
import pytest
import requests
from selenium import webdriver

from config.Conf import Configdata

_driver = None


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def driver():
    global _driver
    if _driver is None:
        _driver = webdriver.Chrome()
        _driver.maximize_window()
    yield _driver


# 在所有的接口请求之前执行
# @pytest.fixture(scope="session",autouse=True)#自动执行
# def clean_extract():
#     print("清理数据")
#     clean_yaml()

def login(mobile, ver_code):
    conf = Configdata()
    url = 'https://demo-api.apipost.cn/api/demo/login'
    payload = {  # 定义请求数据
        'mobile': mobile,
        'ver_code': ver_code
    }
    # headers = {'Content-Type': 'application/json'}
    # json_data = json.dumps(payload)  # 转换为json格式
    # 发送POST请求
    response = requests.post(url=url, data=payload)
    result = response.json()

    # write_yaml({"token": result['data']['token']})
    # token = Configdata.get_conf_token(conf)['token']

    return response


# encoding:utf-8
import pytest


@pytest.fixture()
def login(request):
    print("\n=======================request start=================================")
    print('测试方法的参数化数据：{}'.format(request.param))
    print('测试方法所处模块的信息：{}'.format(request.module))
    print('测试方法信息：{}'.format(request.function))
    print('测试方法所在的类的信息：{}'.format(request.cls))
    print('测试方法所在路径信息：{}'.format(request.fspath))
    print('测试方法调用的多个fixture函数（比如fixture函数之间的嵌套调用（包括pytest内嵌的fixture函数））信息：{}'.format(request.fixturenames))
    print('测试方法调用的单个fixture函数（自己在程序中定义在测试方法中调用的fixture函数）信息：{}'.format(request.fixturename))
    print('测试方法级别信息：{}'.format(request.scope))
    print("\n=======================request end=================================")

# if __name__ == '__main__':
#     conf = Configdata()
#     # print(login(testdemo().get_mobile(),testdemo().get_ver_code()).json())
#     url = 'https://demo-api.apipost.cn/api/demo/news_list?mobile=18289454846&theme_news=国际新闻&page=1&pageSize=20'
#     # data = {'mobile': 18289454846, 'ver_code': 123456}
#     token = Configdata.get_conf_token(conf)['token']
#     headers ={
#         # 'Content-Type': 'application/json',
#         'token': token
#     }
#     re = Request.requests_api(url=url, methon="get", headers=headers)
#
#     # print(re.json())
#     print(re)
