#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: loggingFactory
@time: 06/06/2018 11:30 AM
'''

import logging


class Log(object):
    def __init__(self, level=logging.DEBUG):
        self.level = level
        logging.basicConfig(level=self.level)

    def getLog(self, name=None):
        return logging.getLogger(name)
