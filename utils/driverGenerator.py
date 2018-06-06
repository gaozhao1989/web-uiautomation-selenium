#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: driverGenerator
@time: 06/06/2018 1:39 PM
'''

import pytest
from selenium import webdriver
from utils import loggingFactory, configParserFactory, pathFactory

log = loggingFactory.Log().getLog('Base')


class DriverGenerator(object):

    @classmethod
    @pytest.fixture(scope="session", autouse=True)
    def driver_generator(self):
        browser = configParserFactory.get_browser_name()
        url = configParserFactory.get_test_url()

        log.info('init the driver:')
        try:
            if browser == 'Chrome':
                self.driver = webdriver.Chrome(pathFactory.get_chrome_driver())
            elif browser == 'Firefox':
                self.driver = webdriver.Firefox(pathFactory.get_gecko_driver())
            elif browser == 'IE':
                self.driver = webdriver.Ie()
            elif browser == 'Edge':
                self.driver = webdriver.Edge()
            elif browser == 'Safari':
                self.driver = webdriver.Safari()
        except:
            log.info('unexcept driver error!')
            self.driver.quit()

        log.info('open url: %s' % url)
        self.driver.get(url)
        log.info('maximize window')
        self.driver.maximize_window()
        log.info('set the implicitly wait to 10 seconds')
        self.driver.implicitly_wait(10)
        log.info('start test')

        yield

        log.info('end text')
        self.driver.quit()
