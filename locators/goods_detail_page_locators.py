#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: goods_detail_page_locators.py
@time: 2019/1/5 下午10:50
'''

from selenium.webdriver.common.by import By


class GoodsDetailPageLocators(object):
    BTN_ADD_TO_CART = (By.ID, 'add-to-cart-button')
