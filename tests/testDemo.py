#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: testDemo
@time: 06/06/2018 3:24 PM
'''

import pytest, allure
from pages import demoPage
from utils import driverGenerator, loggingFactory

log = loggingFactory.Log().getLog('Demo')


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('user')
@allure.story('demo')
class TestDemo(driverGenerator.DriverGenerator):

    @allure.step(title='test_demo_01')
    def test_demo_01(self):
        demo_page = demoPage.Demo(self.driver)
        assert demo_page.is_page_exist()
        demo_page.take_screen_shot('DemoPage')
        demo_page.set_input_text_field('Demo Test For Lu')
        assert demo_page.click_search_btn().is_page_exist()
