#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: pathFactory
@time: 06/06/2018 9:54 PM
'''

import os

from utils import configParserFactory


def current_path():
    return os.getcwd()


def get_workspace_root_path():
    workspace_name = configParserFactory.get_workspace_name()
    present_work_dir = current_path()
    while True:
        if present_work_dir.endswith(workspace_name):
            break
        else:
            present_work_dir = os.path.dirname(present_work_dir)
    return present_work_dir


def get_abs_path(path):
    return os.path.abspath(path)


def get_config_file_path():
    return get_abs_path(path_join(get_workspace_root_path(), 'config', 'config.ini'))


def _get_driver():
    return get_abs_path(path_join(get_workspace_root_path(), 'drivers'))


def get_chrome_driver():
    return get_abs_path(_get_driver(), 'chromedriver')


def get_gecko_driver():
    return get_abs_path(_get_driver(), 'geckodriver')


def path_join(path, *paths):
    return os.path.join(path, *paths)


def make_dir(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
