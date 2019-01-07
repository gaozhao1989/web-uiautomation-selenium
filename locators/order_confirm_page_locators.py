#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: order_confirm_page_locators.py
@time: 2019/1/5 下午11:01
'''

from selenium.webdriver.common.by import By


class OrderConfirmPageLocators(object):
    TEXT_ORDER_CONFIRM_MSG = (By.XPATH, '//*[@id="huc-v2-order-row-confirm-text"]/h1')

    TEXT_ORDER_CONFIRM_PRICE = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')
