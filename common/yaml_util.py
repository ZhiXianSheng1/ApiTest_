import os
import yaml
#读取
# def read_yaml(key):
#     with open(os.getcwd()+'/configdata.yaml',mode='r',encoding='utf-8') as f:
#         value = yaml.safe_load(f)
#         return value[key]

import os
#创建类
class YamlReader:
#2.初始化。文件是否存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
#3.yaml读取
    def read_data(self):
        #第一次调用data,读取yaml文档。如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
            return self._data

    # 写入
    def write_yaml(data):
        with open(os.getcwd() + '/data.yaml', mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除
    def clean_yaml(data={}):
        with open(os.getcwd() + '/data.yaml', mode='w', encoding='utf-8') as f:
            f.truncate()