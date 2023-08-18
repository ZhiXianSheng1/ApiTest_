# 1.导入logging包
import logging

# 2.配置信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# 3.定义日志名称getlogger
logger = logging.getLogger("log_demo")
# 4.info,  self.log.debug("ads")
logger.info("info")
logger.debug("debug")
logger.warning("warning")
