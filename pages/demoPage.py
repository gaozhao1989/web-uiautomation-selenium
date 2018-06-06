#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: demoPage
@time: 06/06/2018 1:23 PM
'''

from pages import basePage
from utils import findByFactory
from pages import demoPage2


class Demo(basePage.Base):
    _by = findByFactory.by

    input_text_field = ('xpath', '//*[@id="kw"]')
    el_input_text_field = _by(input_text_field[0]), input_text_field[1]

    search_btn = ('xpath', '//*[@id="su"]')
    el_search_btn = _by(search_btn[0]), search_btn[1]

    def is_page_exist(self):
        return self.is_exist(self.el_search_btn)

    def set_input_text_field(self, text):
        self.input(self.el_input_text_field, text)

    def click_search_btn(self):
        self.click(self.el_search_btn)
        return demoPage2.Demo2(self.driver)
