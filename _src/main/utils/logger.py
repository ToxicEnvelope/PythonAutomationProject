#!/usr/bin/env python3
import logging
import coloredlogs
from _src.main.config.global_config import GlobalConfig


class Logger:

    def __init__(self, namespace):
        self.__log = None
        logging.basicConfig(filename='{0}/{1}-runtime.log'.format(GlobalConfig.get_logs_dir(),
                                                                  GlobalConfig.get_timestamp()),
                            filemode='a',
                            format='%(asctime)s%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
        if self.__log is None:
            self.__log = logging.getLogger(namespace)
        coloredlogs.install(level='DEBUG', logger=self.__log, programname=namespace)

    def info(self, msg):
        self.__log.info(msg)

    def warn(self, msg):
        self.__log.warning(msg)

    def critical(self, msg):
        self.__log.critical(msg)

    def error(self, msg):
        self.__log.error(msg)

    def debug(self, msg):
        self.__log.debug(msg)


if __name__ == '__main__':
    l = Logger(__name__)
    l.info('test info')
    l.warn('test warning')
    l.critical('test critical')
    l.error('test error')
    l.debug('test debug')
