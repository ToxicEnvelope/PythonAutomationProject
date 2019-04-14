#!/usr/bin/env python3
import os
from time import time


class GlobalConfig:

    @staticmethod
    def get_logs_dir():
        root = os.path.expanduser('~/Desktop/Git/NewPythonProject')
        return '{0}/_src/logs'.format(root)

    @staticmethod
    def get_resources_dir():
        root = os.path.expanduser('~/Desktop/Git/NewPythonProject')
        return '{0}/_src/tests/resources'.format(root)

    @staticmethod
    def get_bin_dir():
        root = os.path.expanduser('C:\\Users\\yahav.hoffman\\Desktop\Git\\NewPythonProject')
        return '{0}/bin'.format(root)

    @staticmethod
    def get_timestamp():
        return time().__str__()[:10]


if __name__ == '__main__':
    GlobalConfig.get_logs_dir()
    GlobalConfig.get_resources_dir()
    GlobalConfig.get_bin_dir()
    GlobalConfig.get_timestamp()
