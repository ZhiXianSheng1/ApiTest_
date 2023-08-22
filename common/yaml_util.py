import os
import sys
import yaml
from common.YamlPath import YamlPath


class YamlReader:
    _data = None
    yamlf = None

    @classmethod
    def handle_key_error(cls, e, name):
        # print(f"错误信息:{e}")
        sys.exit(1)

    # 3.yaml读取
    @classmethod
    def read_data(cls, yamlf):
        # 2.初始化。文件是否存在
        if os.path.exists(yamlf):
            cls.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        cls._data = None
        # 第一次调用data,读取yaml文档。如果不是，直接返回之前保存的数据
        if not cls._data:
            with open(cls.yamlf, "rb") as f:
                cls._data = yaml.safe_load(f)
            return cls._data

    @classmethod
    def read_yaml1(cls, yamlf):
        file = open(yamlf, 'r', encoding='utf-8')
        with file as doc:
            content = yaml.load(doc, Loader=yaml.Loader)
            return content

    @classmethod
    def read_case(cls, yaml_name):
        if yaml_name not in YamlPath.yaml_dirpath():
            print('\033[91m' + f"{yaml_name}未定义,请检查!" + '\033[0m')  # 改变打印的颜色
        try:
            fp = YamlPath.yaml_dirpath()[yaml_name]
        except KeyError as e:
            cls.handle_key_error(e, yaml_name)
        else:
            case_data = cls.read_data(YamlPath.yaml_dirpath()[f'{yaml_name}'])
            # print(case_data)

            for k, v in case_data.items():  # 将yaml第一行的用例标题移到字典里，赋名case_name
                case_title = k
                if v['is_run'] == True:
                    v['case_name'] = case_title
                    yield v

    # 写入
    def write_yaml(self, data):
        with open(self.yamlf, 'w') as f:
            try:
                yaml.dump(data, f) == True
            except Exception as e:
                return print("写入出现异常了" + e)
        return data

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
