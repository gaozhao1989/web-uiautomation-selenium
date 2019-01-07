#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: base_Page.py
@time: 06/06/2018 11:24 AM
'''
from utils.log import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from utils import path_parser

import datetime
import time


class BasePage(object):
    '''
    Base page. All other page should inherit from this class. Contains common actions from webdriver.
    '''

    def __init__(self, driver):
        self.driver = driver
        self.log = Log().getlog('Base')

    def go(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def execute(self, command, params=None):
        self.driver.execute(command, params)

    def current_url(self):
        return self.driver.current_url

    def page_source(self):
        return self.driver.page_source

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def max(self):
        self.driver.maximize_window()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_cookie3(self):
        self.driver.delete_all_cookies()

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def set_loc_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def set_script_wait(self, sec):
        self.driver.set_script_timeout(sec)

    def set_page_wait(self, sec):
        self.driver.set_page_load_timeout(sec)

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_window_size(self):
        return self.driver.get_window_size()

    def set_window_position(self, x, y):
        self.driver.set_window_position(x, y)

    def get_window_position(self):
        return self.driver.get_window_position()

    def get_window_rect(self):
        return self.driver.get_window_rect()

    def set_window_rect(self, x=None, y=None, width=None, height=None):
        self.driver.set_window_rect(x, y, width, height)

    def find(self, loc):
        self.log.info('try to find element by \'{}\' with \'{}\' in page'.format(*loc))
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            self.log.info('no element by \'{}\' with \'{}\' was found in page'.format(*loc))

    def finds(self, loc):
        self.log.info('try to find elements by \'{}\' with \'{}\' in page'.format(*loc))
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            self.log.info('no elements by \'{}\' with \'{}\' was found in page'.format(*loc))

    def wait(self, loc, sec):
        WebDriverWait(self.driver, sec).until(lambda driver: self.find(loc))

    def take_screen_shot(self, name):
        date_format = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        pf = path_parser.PathParser()
        screenshots_path = pf.get_abs_path(
            pf.path_join(pf.get_workspace_root_path(), 'screenshots'))
        screenshots_name = ''.join([date_format, name, '.png'])
        pf.make_dir(screenshots_path)
        self.driver.get_screenshot_as_file(
            pf.path_join(screenshots_path, screenshots_name))

    def is_displayed(self, loc):
        return self.find(loc).is_displayed()

    def click(self, loc):
        self.find(loc).click()

    def send_keys(self, loc, text='', clear_content=True):
        el = self.find(loc)
        if clear_content:
            el.clear()
        el.send_keys(text)

    def get_text(self, loc):
        return self.find(loc).text

    @staticmethod
    def sleep(sec=3):
        time.sleep(sec)

    def implicitly_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles
