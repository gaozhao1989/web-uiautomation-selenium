#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: findByFactory
@time: 06/06/2018 11:46 AM
'''

from selenium.webdriver.common.by import By


def by(by):
    by = by.lower()
    if by == 'id':
        return By.ID
    elif by == 'xpath':
        return By.XPATH
    elif by == 'link_text':
        return By.LINK_TEXT
    elif by == 'partial_link_text':
        return By.PARTIAL_LINK_TEXT
    elif by == 'name':
        return By.NAME
    elif by == 'tag_name':
        return By.TAG_NAME
    elif by == 'class_name':
        return By.CLASS_NAME
    elif by == 'css_selector':
        return By.CSS_SELECTOR
