#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: testDemo2
@time: 08/06/2018 8:46 PM
'''

import pytest, allure
from pages import demopage
from utils import drivergenerator, loggingfactory

log = loggingfactory.Log().getlog('Demo2')


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('user')
@allure.story('demo2')
class TestDemo2(drivergenerator.DriverGenerator):

    @allure.step(title='test_demo2_01')
    def test_demo2_01(self):
        demo_page = demopage.Demo(self.driver)
        demo_page.set_input_text_field('Demo Test For Lu')
        demo_page2 = demo_page.click_search_btn()
        assert demo_page2.is_page_exist()
