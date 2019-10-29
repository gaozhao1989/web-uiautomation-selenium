#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: 449628536@qq.com
@software: web-uiautomation-selenium
@file: test_order.py
@time: 2019/1/5 下午5:34
'''

import pytest
from pages import main_page


# pytest get the registered attr driver
@pytest.mark.usefixtures('driver')
class TestDemo(object):

    def test_01_order(self, order_price_fixture):
        main = main_page.MainPage(self.driver)
        main.wait_page_present()
        main.set_text_nav_search_text_box('软件测试')
        search_results = main.click_nav_search_text_btn()
        search_results.wait_page_persent()
        order_confirm = search_results.click_product_book_st_second_ver_in_results().click_add_to_cart_btn()
        assert order_confirm.get_order_confirm_msg() == '商品已加入购物车'
        assert order_confirm.get_order_confirm_price() == order_price_fixture
