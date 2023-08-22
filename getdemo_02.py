from common.Requests_util import Request
from common.ParameterSetting import YamlTemplate
from config.Conf import YamlReader, ConfigYaml
import requests
import os

conf = ConfigYaml()
mobile1 = conf.get_conf_mobile()
ver_code1 = conf.get_conf_vercode()
import yaml
import jinja2


def get_token1():
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
    return token_value


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_yaml_path = os.path.join(current_dir, "test.yaml")
    template = YamlTemplate(test_yaml_path)
    rendered = template.render()
    print(rendered)
