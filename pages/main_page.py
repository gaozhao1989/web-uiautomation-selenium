#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: main_page.py
@time: 2019/1/5 下午4:48
'''

from pages import base_page, search_results_page
from locators.main_page_locators import MainPageLocators


class MainPage(base_page.BasePage):

    def click_nav_search_text_box(self):
        self.click(MainPageLocators.TEXT_NAV_SEARCH_TEXT_BOX)

    def click_nav_search_text_btn(self):
        self.click(MainPageLocators.SUBMIT_NAV_SEARCH_TEXT_BTN)
        return search_results_page.SearchResultsPage(self.driver)

    def set_text_nav_search_text_box(self, text=''):
        self.send_keys(MainPageLocators.TEXT_NAV_SEARCH_TEXT_BOX, text)
