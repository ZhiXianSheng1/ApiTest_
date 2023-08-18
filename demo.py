from common.yaml_util import YamlReader
from config.Conf import ConfigYaml, get_datayaml_file
from config.Conf import Configdata
from conftest import get_token

# data = {'name': 'zhangsan','mobile': '1241442'}
conf = Configdata()
conf_yaml = ConfigYaml()
# a= conf1.get_conf_headersC()
# def get_news_talk():
# re = Request.requests_api(method="post", url=conf_yaml.get_conf_urls()["url_news_talk"],
#                               headers={
#                                        'token': Configdata.get_conf_token(Configdata())['token']},
#                               data= conf_yaml.get_conf_data())
#
# print(re)
YamlReader(get_datayaml_file()).clean_yaml(get_token())
# print(conf.get_conf_token()['token'])
# print(YamlReader(get_config_file()).read_data()["talk"])
