import os


class FilePath:
    @classmethod
    def params_filepath(cls):
        """
        存放参数依赖、提取得公共池
        :return:
        """
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "params_pool.ini")
        return file_path
