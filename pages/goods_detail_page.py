#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: goods_detail_page.py
@time: 2019/1/5 下午10:55
'''

from pages import base_page, order_confirm_page
from locators.goods_detail_page_locators import GoodsDetailPageLocators


class GoodsDetailPage(base_page.BasePage):

    def is_page_displayed(self):
        return self.is_displayed(GoodsDetailPageLocators.BTN_ADD_TO_CART)

    def click_add_to_cart_btn(self):
        self.click(GoodsDetailPageLocators.BTN_ADD_TO_CART)
        return order_confirm_page.OrderConfirmPage(self.driver)
