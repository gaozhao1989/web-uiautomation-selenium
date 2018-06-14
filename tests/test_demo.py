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
from pages import demopage
from utils import drivergenerator, loggingfactory

log = loggingfactory.Log().getlog('Demo')


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('user')
@allure.story('demo')
class TestDemo(drivergenerator.DriverGenerator):

    @allure.step(title='test_demo_01')
    def test_demo_01(self):
        demo_page = demopage.Demo(self.driver)
        assert demo_page.is_page_exist()
        demo_page.take_screen_shot('DemoPage')
        demo_page.set_input_text_field('Demo Test For Lu')
        demo_page2 = demo_page.click_search_btn()
        assert demo_page2.is_page_exist()
        demo_page2.back_to_demo_page()

    @allure.step(title='test_demo_02')
    def test_demo_02(self):
        demo_page = demopage.Demo(self.driver)
        assert demo_page.get_title() == '123'
