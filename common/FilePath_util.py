import os

from common.yaml_util import YamlReader


class FilePath:
    current = os.path.abspath(__file__)  # 当前路径
    BASE_DIR = os.path.dirname(os.path.dirname(current))  # 基础路径

    @classmethod
    def yaml_name(cls, yamlname):
        config = YamlReader().read_case(yamlname)
        return config

    @classmethod
    def params_filepath(cls):
        """
        存放参数依赖、提取得公共池
        :return:
        """
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "params_pool.ini")
        return file_path

    @classmethod
    def get_log_path(cls):
        _log_path = cls.BASE_DIR + os.sep + "logs"
        """
        获取log文件路径
        :return:
        """
        return _log_path
