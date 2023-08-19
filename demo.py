import json

import pytest
import requests

from config.Conf import ConfigYaml, get_datayaml_file
from config.Conf import Configdata, YamlReader, get_test01_file
from common.Requests_util import Request

conf = Configdata()
conf_yaml = ConfigYaml()


@pytest.mark.parametrize("cr_getdatalist", YamlReader(get_test01_file()).read_data()[0:1])
def get_datalists(cr_getdatalist):
    url = cr_getdatalist["request"]["url"]
    headers = cr_getdatalist["request"]["headers"]
    headers["token"] = YamlReader(get_datayaml_file()).read_data()["token"]
    method = cr_getdatalist["request"]["method"]
    data = cr_getdatalist["request"]["params"]
    re = Request.requests_api(method=method, url=url, data=data, headers=headers)
    yield re


class tools_news:
    @pytest.mark.parametrize("cr_getdatalist", YamlReader(get_test01_file()).read_data()[0:1])
    def get_news_datalists(cr_getdatalist):
        url = cr_getdatalist["request"]["url"]
        headers = cr_getdatalist["request"]["headers"]
        headers["token"] = YamlReader(get_datayaml_file()).read_data()["token"]
        method = cr_getdatalist["request"]["method"]
        data = cr_getdatalist["request"]["params"]
        re = Request.requests_api(method=method, url=url, data=data, headers=headers)
        yield re

    @pytest.mark.parametrize("cr_getdatalist", YamlReader(get_test01_file()).read_data()[1:2])
    def get_news_data(cr_getdatalist):
        url = cr_getdatalist["request"]["url"]
        headers = cr_getdatalist["request"]["headers"]
        headers["token"] = YamlReader(get_datayaml_file()).read_data()["token"]
        method = cr_getdatalist["request"]["method"]
        data = cr_getdatalist["request"]["params"]
        re = Request.requests_api(method=method, url=url, data=data, headers=headers)
        print(re)

    @pytest.mark.parametrize("cr_getdatalist", YamlReader(get_test01_file()).read_data()[1:2])
    def get_news_collect(cr_getdatalist):
        url = cr_getdatalist["request"]["url"]
        headers = cr_getdatalist["request"]["headers"]
        headers["token"] = YamlReader(get_datayaml_file()).read_data()["token"]
        method = cr_getdatalist["request"]["method"]
        data = cr_getdatalist["request"]["params"]
        re = Request.requests_api(method=method, url=url, data=data, headers=headers)
        print(re)
