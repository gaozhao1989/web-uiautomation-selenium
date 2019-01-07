#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: search_results_page.py
@time: 2019/1/5 下午5:22
'''

from pages import base_page, goods_detail_page
from locators.search_results_page_locators import SearchResultPageLocators


class SearchResultsPage(base_page.BasePage):

    def is_page_displayed(self):
        return self.is_displayed(SearchResultPageLocators.UL_SEARCH_RESULTS_LIST)

    def click_product_book_st_second_ver_in_results(self):
        # broswer open in new tab, switch to new tab
        search_results_handle = self.get_current_window_handle()
        self.click(SearchResultPageLocators.GOODS_BOOK_ST_SECOND_VER)
        for handle in self.get_window_handles():
            if handle != search_results_handle:
                self.switch_to_window(handle)
        return goods_detail_page.GoodsDetailPage(self.driver)
