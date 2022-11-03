import logging

import coloredlogs
from config.config import Config

LOG_LEVEL = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}


logger = logging.getLogger(Config.APP_NAME)
log_format = "[%(asctime)s|%(processName)10s|%(threadName)10s|%(levelname)7s|%(filename)s:%(lineno)03d] %(message)s"
coloredlogs.install(
    logger=logger,
    milliseconds=True,
    fmt=log_format,
    level=LOG_LEVEL[Config.LOGGING_LEVEL],
)
