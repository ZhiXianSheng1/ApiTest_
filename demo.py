import json

import requests

from config.Conf import ConfigYaml
from config.Conf import Configdata

# data = {'name': 'zhangsan','mobile': '1241442'}
conf = Configdata()
conf_yaml = ConfigYaml()
# a= conf1.get_conf_headersC()
# def get_news_talk():
# re = Request.requests_api(method="delete", url= conf_yaml.get_conf_urls()["url_news_delete"],
#                               headers={'Content-Type': conf_yaml.get_conf_headersC(),
#                                        'token': Configdata.get_conf_token(Configdata())['token']})
# YamlReader(get_datayaml_file()).clean_yaml(get_token())
# print(conf.get_conf_token()['token'])
# print(re)
# print(YamlReader(get_config_file()).read_data()["talk"])

url = "https://demo-api.apipost.cn/api/demo/delete_comment"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODI4OTQ1NDg0NiIsInZlcl9jb2RlIjoi8J6JgCIsImV4cCI6MTY5MjQwMDg1OSwiaXNzIjoicHJvOTExIn0.6hp2eJxSu6fwHbej-LsGGVkU-gTZq-DZQb8Mve807bM"
headers = {
    'token': token
}
payload = {
    "id": 20,
    "comment_id": 98
}
parmas = json.dumps(payload)
aa = json.dumps(conf_yaml.get_conf_delete())
print(aa)
res = requests.delete(url=url, data=parmas, headers=headers)
print(res.json())
