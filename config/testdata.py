from common.yaml_util import YamlReader
from config.Conf import get_config_file


class testdemo:
    # 初始化yaml读取文件的路径
    def __init__(self):
        self.config = YamlReader(get_config_file()).read_data()

    # 定义方法获取需要信息
    def get_mobile(self):
        return self.config["BASE"]["mobile"]  # 获取通用mobile

    def get_ver_code(self):
        return self.config["BASE"]["ver_code"]  # 获取通用ver_code


if __name__ == '__main__':
    conf_read = testdemo().get_mobile()
    conf_read1 = testdemo().get_ver_code()
    # conf_read2 = Configdata().get_conf_token()

    print(conf_read)
    print(conf_read1)
    print(YamlReader(get_config_file()).read_data())
