import os
class FilePath:
    current = os.path.abspath(__file__)  # 当前路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(current)))  # 基础路径
    @classmethod
    def yaml_name(cls, yamlname):
        from common.yaml_common.yaml_util import YamlReader
        config = YamlReader().read_case(yamlname)
        return config
    @classmethod
    def params_filepath(cls):
        """
        存放参数依赖、提取得公共池
        :return:
        """
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "../params_pool.ini")
        return file_path

    @classmethod
    def get_log_path(cls):
        _log_path = cls.BASE_DIR + os.sep + "logs"
        """
        获取log文件路径
        :return:
        """
        return _log_path

    @classmethod
    def yaml_dirpath(cls):
        yaml_files = {}
        _testcase_path = cls.BASE_DIR + os.sep + "test_case"
        for root, dirs, files in os.walk(_testcase_path):  # root 根路径
            for filename in files:
                if filename.endswith(".yaml"):
                    yaml_file = os.path.join(root, filename)
                    yaml_dict = {filename: yaml_file}
                    # print(yaml_dict)
                    yaml_files.update(yaml_dict)
        return yaml_files
