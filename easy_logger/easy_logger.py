#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# author: John Deng


import logging, logging.handlers
import settings  

LOG_FORMAT = "%(name)s %(process)d %(processName)s %(asctime)s %(levelname)s %(message)s" 

def easy_logger():
    """ wapper the logging. 
    """
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    formatter = logging.Formatter(LOG_FORMAT)
    handler = logging.handlers.TimedRotatingFileHandler(settings.log_path, when='d', interval=1)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
