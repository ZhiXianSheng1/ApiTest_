import datetime
import inspect
import logging
# 定义日志级别的映射
import os.path
# from common.file_common.FilePath_util import FilePath
from colorlog import ColoredFormatter
# 封装log工具类
# 1.创建类
from common.file_common.FilePath_util import FilePath
from common.log_common.log_colorConfig import log_levels, log_colors


class Logger:
    """2.定义参数,输出文件名称，loggername,日志级别"""
    logger_instance = None

    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level
        """1、设置logger名称"""
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_levels[self.log_level])
        """清空日志句柄列表"""
        self.logger.handlers.clear()
        """输出到控制台"""
        if self.log_level != 'INFO':
            self.add_console_handler()
        """写入文件"""
        self.add_file_handler()

    """控制台输出日志"""

    def add_console_handler(self):
        fh_stream_formatter = ColoredFormatter('%(asctime)s %(log_color)s%(name)s %(levelname)s %(message)s',
                                               log_colors=log_colors)
        fh_stream = logging.StreamHandler()
        fh_stream.setLevel(log_levels[self.log_level])
        fh_stream.setFormatter(fh_stream_formatter)
        self.logger.addHandler(fh_stream)
        """文件输出日志"""

    def add_file_handler(self):
        fh_file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        fh_file = logging.FileHandler(self.log_file, encoding='utf-8')
        fh_file.setLevel(log_levels[self.log_level])
        fh_file.setFormatter(fh_file_formatter)
        self.logger.addHandler(fh_file)

    def generate_log_file(self):
        log_path = FilePath().get_log_path()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        log_extension = ".log"
        log_file = os.path.join(log_path, current_time + log_extension)
        return log_file

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
        cls.logger_instance = cls(log_file=cls.generate_log_file(cls), log_name=log_name, log_level=log_level).logger
        return cls.logger_instance
# if __name__ == '__main__':
#     Logger.my_log().info("INFO   输出")
#     Logger.my_log(log_level='WARNING').warning("WARNING   输出")
#     Logger.my_log(log_level='ERROR').error("ERROR   输出")
#     Logger.my_log(log_level='DEBUG').debug("DEBUG   输出")
