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

from utils import path_parser


class ConfigParser:

    def __init__(self):
        self.config_file_path = path_parser.PathParser().get_config_file_path()
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_browser_name(self):
        return self.config.get("BROSWER", "broswerName")

    def get_test_url(self):
        return self.config.get('TEST-URL', 'url')

    def get_implicitly_wait(self):
        return self.config.get('IMPLICITLY-WAIT', 'implicitlyWait')

    def get_rerun_failures(self):
        return self.config.get('RERUN-FAILURES', 'rerunFailures')

    def get_rerun_delay(self):
        return self.config.get('RERUN-DELAY', 'rerunDelay')
