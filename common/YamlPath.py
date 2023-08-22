import os


class YamlPath:
    @classmethod
    def yaml_dirpath(cls):
        yaml_files = {}
        current = os.path.abspath(__file__)  # 当前路径
        BASE_DIR = os.path.dirname(os.path.dirname(current))  # 基础路径
        # print(BASE_DIR)
        _testcase_path = BASE_DIR + os.sep + "test_case"
        # print(_testcase_path)
        for root, dirs, files in os.walk(_testcase_path):
            for filename in files:
                if filename.endswith(".yaml"):
                    yaml_file = os.path.join(root, filename)
                    yaml_dict = {filename: yaml_file}
                    # print(yaml_dict)
                    yaml_files.update(yaml_dict)
        return yaml_files
