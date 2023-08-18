import pytest

from common.Requests_util import Request
from common.yaml_util import YamlReader
from config.Conf import get_datayaml_file, ConfigYaml

conf = ConfigYaml()
mobile1 = conf.get_conf_mobile()
ver_code1 = conf.get_conf_vercode()


# _driver = None
# 在所有的接口请求之前执行 清理data.yaml 数据
@pytest.fixture(scope="session", autouse=True)
def connection_mysql(get_token):
    token_data = get_token
    print("之前：连接数据库")
    yield YamlReader(get_datayaml_file()).clean_yaml(token_data)


@pytest.fixture(scope="session")
def get_token():
    mobile = mobile1
    ver_code = ver_code1
    re = Request.requests_api(method="post",
                              url='https://demo-api.apipost.cn/api/demo/login',
                              data={  # 定义请求数据
                                  'mobile': mobile,
                                  'ver_code': ver_code
                              }
                              )
    token_value = re["body"]["data"]["token"]
    token = {'token': token_value}
    # write_yaml =YamlReader(get_datayaml_file()).write_yaml(token)
    return token

# if __name__ == '__main__':
#     conf =ConfigYaml()
#     print(get_token(ConfigYaml.get_conf_mobile(conf),ConfigYaml.get_conf_vercode(conf)))#获取token
# token = Configdata.get_conf_token(conf)['token']


# encoding:utf-8
# import pytest


# @pytest.fixture()
# def login(request):
#     print("\n=======================request start=================================")
#     print('测试方法的参数化数据：{}'.format(request.param))
#     print('测试方法所处模块的信息：{}'.format(request.module))
#     print('测试方法信息：{}'.format(request.function))
#     print('测试方法所在的类的信息：{}'.format(request.cls))
#     print('测试方法所在路径信息：{}'.format(request.fspath))
#     print('测试方法调用的多个fixture函数（比如fixture函数之间的嵌套调用（包括pytest内嵌的fixture函数））信息：{}'.format(request.fixturenames))
#     print('测试方法调用的单个fixture函数（自己在程序中定义在测试方法中调用的fixture函数）信息：{}'.format(request.fixturename))
#     print('测试方法级别信息：{}'.format(request.scope))
#     print("\n=======================request end=================================")


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     获取每个用例状态的钩子函数
#     :param item:
#     :param call:
#     :return:
#     """
#     # 获取钩子方法的调用结果
#     outcome = yield
#     rep = outcome.get_result()
#     # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         # 添加allure报告截图
#         if hasattr(_driver, "get_screenshot_as_png"):
#             with allure.step('添加失败截图...'):
#                 allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# @pytest.fixture(scope='session')
# def driver():
#     global _driver
#     if _driver is None:
#         _driver = webdriver.Chrome()
#         _driver.maximize_window()
#     yield _driver
# @pytest.mark.parametrize("get_mobile", "get_ver_code")
