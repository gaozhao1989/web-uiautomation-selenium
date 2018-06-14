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

from utils import pathparserfactory


class ConfigParser:

    def __init__(self):
        self.config_file_path = pathparserfactory.PathParser().get_config_file_path()
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_browser_name(self):
        return self.config.get("BROSWER", "broswerName")

    def get_test_url(self):
        return self.config.get('TEST-URL', 'url')

    def get_test_scope(self):
        return self.config.get('TEST-SCOPE', 'testScope')

    def get_workspace_name(self):
        return self.config.get('WORKSPACE', 'workSpaceName')
