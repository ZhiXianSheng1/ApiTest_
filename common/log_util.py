import datetime
import logging
# 定义日志级别的映射
import os.path

import config.Conf
from config import Conf
from config.Conf import ConfigYaml

log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# 封装log工具类
# 1.创建类
class Logger:
    # 2.定义参数
    # 输出文件名称，loggername,日志级别
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level
        # 3.编写输出控制台或文件
        # 输出控制台
        # 1、设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 2、设置log级别
        self.logger.setLevel(log_l[self.log_level])  # logger.INFO
        # 判断handlers是否存在
        if not self.logger.handlers:
            # 3、输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)
            # 写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 6、添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
            # 7、运行输出
            # self.logger.info("this is info")
            # self.logger.debug("this is debug")
            # self.logger.warning("this is waring")


# 1、初始化参数数据
# 日志文件名称，日志文件级别
# 日志文件名称 = logs目录 + 当前时间 + 扩展名
# log目录
log_path = Conf.get_log_path()
# 当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# 扩展名
log_extension = config.Conf.ConfigYaml().get_conf_log_extension()
logfile = os.path.join(log_path, current_time + log_extension)
# print(logfile)
# 日志文件级别
logleavel = ConfigYaml().get_conf_log()


# print(logleavel)
# 2.对外方法，初始log工具包，提供其他类使用
def my_log(log_name=__file__):  # 给默认值
    return Logger(log_file=logfile, log_name=log_name, log_level=logleavel).logger


if __name__ == '__main__':
    my_log().debug("this is aaa")
    my_log().warning("this is aaa")
