#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: demoPage2
@time: 06/06/2018 4:54 PM
'''

from pages import basePage
from utils import findByFactory


class Demo2(basePage.Base):
    _by = findByFactory.by

    results_content_div = ('id', 'content_left')
    el_results_content_div = _by(results_content_div[0]), results_content_div[1]

    releated_results_div = ('id', 'con-ar')
    el_releated_results_div = _by(releated_results_div[0]), releated_results_div[1]

    def is_page_exist(self):
        return self.is_exist(self.el_results_content_div)

