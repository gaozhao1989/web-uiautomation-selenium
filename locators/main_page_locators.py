#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2019.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: main_page_locators.py
@time: 04/01/2019 8:21 PM
'''

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    '''
    A class for main page locators. All main page locators should come here
    '''

    TEXT_NAV_SEARCH_TEXT_BOX = (By.ID, 'twotabsearchtextbox')

    SUBMIT_NAV_SEARCH_TEXT_BTN = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')
