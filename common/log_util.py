import datetime
import inspect
import logging
# 定义日志级别的映射
import os.path
from common.FilePath_util import FilePath

log_levels = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR
}


# 封装log工具类
# 1.创建类
class Logger:
    # 2.定义参数
    # 输出文件名称，loggername,日志级别
    logger_instance = None

    def __init__(self, log_file, log_name, log_level):

        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        # 1、设置logger名称
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_levels[self.log_level])
        # 清空日志句柄列表
        self.logger.handlers.clear()

        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

        # 输出到控制台
        if self.log_level != 'INFO':
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_levels[self.log_level])
            # print(self.log_level)
            fh_stream.setFormatter(formatter)
            self.logger.addHandler(fh_stream)
        # 写入文件
        fh_file = logging.FileHandler(self.log_file)
        fh_file.setLevel(log_levels[self.log_level])
        fh_file.setFormatter(formatter)
        self.logger.addHandler(fh_file)

    @classmethod
    def my_log(cls, log_name=None, log_level=None):

        if log_name is None:
            caller_frame = inspect.currentframe().f_back
            caller_filename = inspect.getframeinfo(caller_frame).filename
            log_name = caller_filename

        if log_level is None:
            log_level = 'INFO'
        else:
            log_level = log_level.upper()

        log_path = FilePath().get_log_path()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        log_extension = ".log"
        log_file = os.path.join(log_path, current_time + log_extension)

        cls.logger_instance = cls(log_file=log_file, log_name=log_name, log_level=log_level).logger
        return cls.logger_instance


if __name__ == '__main__':
    Logger.my_log().info("INFO   输出")
    Logger.my_log(log_level='WARNING').warning("WARNING   输出")
    Logger.my_log(log_level='ERROR').error("ERROR   输出")
    Logger.my_log(log_level='DEBUG').debug("DEBUG   输出")
