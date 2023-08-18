import os

import yaml


# 创建类
class YamlReader:
    def __int__(self, yamlf):
        self.yamlf = yamlf

    def load_yaml(self):
        with open(self.yamlf, "r") as f:
            data = yaml.safe_load(f)
        return data

    # 2.初始化。文件是否存在
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None

    # 3.yaml读取
    def read_data(self):
        # 第一次调用data,读取yaml文档。如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data = yaml.safe_load(f)
            return self._data

    # 写入
    def write_yaml(self, data):
        with open(self.yamlf, 'w') as f:
            try:
                yaml.dump(data, f) == True
            except Exception as e:
                return print("写入出现异常了" + e)
        return data

    # def write_yaml(self,_data):
    #     with open(self.yamlf,"rb") as f:
    #         self._data = yaml.dump(f)
    #     return self._data
    # # def write_yaml(data):
    # #     with open(os.getcwd() + '/data.yaml', mode='a', encoding='utf-8') as f:
    # #         value = yaml.dump(data=data, stream=f, allow_unicode=True)
    #
    # 清除
    """
    在clean方法中判断保留token键值对
    优点:
    
    逻辑简单直观
    少量更改现有代码
    缺点:
    
    如果有其他重要数据,也需要类似判断
        
        
    """

    def clean_yaml(self, data):
        if "token" in data:
            token_data = {"token": data["token"]}  # 创建新的字典保存包含键值对"token"的数据
            data = {}  # 清空原始数据
            data.update(token_data)  # 将token数据添加回去
        with open(self.yamlf, "w") as f:
            yaml.dump(data, f)
        return data


"""
    def clean_yaml(self):
        data = yaml.load(yamlfile) 
        data.update({"token": data["token"]})
  
        with open(yamlfile, "w") as f:
            yaml.dump(data, f)
2.读取旧配置并更新选择内容
优点:

可以灵活选择保留的键
clean方法只负责清空
缺点:

需要处理读取旧配置的逻辑
更新方式可能不太优雅

"""

# if __name__ == '__main__':
#     conf =ConfigYaml()
#     print(ConfigYaml.get_conf_url(conf))
# ye = YamlReader()
# ye.clean_yaml(ye)
