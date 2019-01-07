#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: search_results_page_locators.py
@time: 2019/1/5 下午11:01
'''

from selenium.webdriver.common.by import By


class SearchResultPageLocators(object):
    UL_SEARCH_RESULTS_LIST = (By.ID, 's-results-list-atf')

    GOODS_BOOK_ST_SECOND_VER = (By.XPATH, '//h2[@data-attribute="软件测试(原书第2版)"]')
