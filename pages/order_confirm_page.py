#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: order_confirm_page.py
@time: 2019/1/5 下午11:00
'''

import re
from pages import base_page
from locators.order_confirm_page_locators import OrderConfirmPageLocators


class OrderConfirmPage(base_page.BasePage):

    def is_page_displayed(self):
        return self.is_displayed(OrderConfirmPageLocators.TEXT_ORDER_CONFIRM_MSG)

    def get_order_confirm_msg(self):
        return self.get_text(OrderConfirmPageLocators.TEXT_ORDER_CONFIRM_MSG)

    def get_order_confirm_price(self):
        return re.search('\\d+.\\d+', self.get_text(OrderConfirmPageLocators.TEXT_ORDER_CONFIRM_PRICE)).group()
