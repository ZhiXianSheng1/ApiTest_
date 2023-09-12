import logging
import os
import time


class Logger:
    def __init__(self, log_name='log.log', log_path=None):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')

        self.file_handler = logging.FileHandler(filename=self.make_file_path(log_name, log_path))
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

        self.console_handler = logging.StreamHandler()
        self.logger.addHandler(self.console_handler)

    @staticmethod
    def make_file_path(log_name, log_path):
        if log_path:
            log_dir = log_path
        else:
            log_dir = os.path.join(os.path.dirname(__file__), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, log_name)

    def set_file_level(self, level):
        self.file_handler.setLevel(level)

    def set_console_level(self, level):
        self.console_handler.setLevel(level)

    def my_log(self, **kwargs):
        level = kwargs.get('log_level')
        if level:
            if level.upper() == 'DEBUG':
                self.logger.setLevel(logging.DEBUG)
            elif level.upper() == 'INFO':
                self.logger.setLevel(logging.INFO)
            elif level.upper() == 'WARNING':
                self.logger.setLevel(logging.WARNING)
            elif level.upper() == 'ERROR':
                self.logger.setLevel(logging.ERROR)
            else:
                self.logger.setLevel(logging.INFO)

        return self.logger


if __name__ == '__main__':
    Logger.my_log(Logger()).info("this is info log")
    Logger.my_log(Logger()).warning("阿达asdad")
    Logger.my_log(Logger(), log_level='ERROR').error("this is error log")
    # Logger.my_log(Logger()).warning("阿达asdad")
    # Logger.my_log(log_level='ERROR').error("this 诗词大赛")
    # Logger.my_log(log_level='ERROR').error("this 诗33词大赛")
