import pytest

from common.Requests_util import Request
from config.Conf import Configdata, ConfigYaml

conf_data = Configdata()
conf_yaml = ConfigYaml()


@pytest.fixture
def get_news_datalists():  # 新闻接口列表
    re = Request.requests_api(method="get",
                              url=conf_yaml.get_conf_urls()["url_news_datalist"],
                              headers={'Content-Type': conf_yaml.get_conf_headersC()})
    yield re


@pytest.fixture
def get_news_data():
    re = Request.requests_api(method="get", url=conf_yaml.get_conf_urls()["url_news_data"],
                              headers={'Content-Type': conf_yaml.get_conf_headersC(),
                                       'token': Configdata.get_conf_token(Configdata())['token']})
    yield re


@pytest.fixture
def get_news_collect():
    re = Request.requests_api(method="post", url=conf_yaml.get_conf_urls()["url_news_collect"],
                              headers={'Content-Type': conf_yaml.get_conf_headersC(),
                                       'token': Configdata.get_conf_token(Configdata())['token']})
    yield re


@pytest.fixture
def get_news_talk():
    re = Request.requests_api(method="post", url=conf_yaml.get_conf_urls()["url_news_talk"],
                              headers={'token': Configdata.get_conf_token(Configdata())['token']},
                              data=conf_yaml.get_conf_data())
    return re

# @pytest.fixture
# def get_news_delete():
#     re = Request.requests_api(methon="get", url= conf_yaml.get_conf_urls()["url_news_delete"],
#                               headers={'Content-Type': conf_yaml.get_conf_headersC(),
#                                        'token': Configdata.get_conf_token(Configdata())['token']})
#     yield re
