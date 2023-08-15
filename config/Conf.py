# 1.获取项目基本目录
# 获取当前项目的绝对路径
import os.path

from common.yaml_util import YamlReader
# 1.获取项目基本目录
# 获取当前项目的绝对路径
import os.path

from common.yaml_util import YamlReader

current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)
# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"  # os.sep 分隔符
# 定义conf.yaml文件的路径
_config_file = _config_path + os.sep + "conf.yaml"
# 定义log文件路径
_log_path = BASE_DIR + os.sep + "logs"

# 定义data.yaml文件路径
_data_token = BASE_DIR + os.sep + "data.yaml"


def get_log_path():
    """
    获取log文件路径
    :return:
    """
    return _log_path


#
def get_datayaml_file():
    """
    获取data.yaml文件路径
    :return:
    """
    return _data_token


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


# 2.读取配置文件
# 创建类
class ConfigYaml:
    # 初始化yaml读取文件的路径
    def __init__(self):
        self.config = YamlReader(get_config_file()).read_data()

    # 定义方法获取需要信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]  # 获取通用url

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]


class Configdata:
    def __init__(self):
        # 初始化yaml读取文件的路径
        self.config = YamlReader(get_datayaml_file()).read_data()

    def get_conf_token(self):
        """
        获取token值
        :return:
        """
        return self.config


if __name__ == '__main__':
    conf_read = ConfigYaml().get_conf_url()
    # conf_read1 = ConfigYaml().get_conf_log_extension()
    # conf_read2 = Configdata().get_conf_token()

    print(conf_read)
    print(YamlReader(get_config_file()).read_data())
    # print(conf_read1)
    # print(conf_read2['token'])
