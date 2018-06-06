#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: configParserFactory
@time: 06/06/2018 1:41 PM
'''

import configparser

from utils import pathFactory

config_file_path = pathFactory.get_config_file_path()
config = configparser.ConfigParser()
config.read(config_file_path)


def get_browser_name():
    return config.get("BROSWER", "broswerName")


def get_test_url():
    return config.get('TEST-URL', 'url')


def get_workspace_name():
    return config.get('WORKSPACE', 'workSpaceName')
