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
from utils import log, config_parser, path_parser

log = log.Log().getlog('Base')


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    cp = config_parser.ConfigParser()
    pp = path_parser.PathParser()
    browser = cp.get_browser_name()
    url = cp.get_test_url()
    implicitly_wait = cp.get_implicitly_wait()

    log.info('init the driver:')
    try:
        if browser == 'Chrome':
            driver = webdriver.Chrome(executable_path=pp.get_chrome_driver())
        elif browser == 'Firefox':
            driver = webdriver.Firefox(executable_path=pp.get_gecko_driver())
        elif browser == 'Edge':
            driver = webdriver.Edge(executable_path=pp.get_ms_edge_driver())
        elif browser == 'Safari':
            driver = webdriver.Safari()
        elif browser == 'Opera':
            driver = webdriver.Opera(executable_path=pp.get_opera_driver())
    except Exception as e:
        log.error('unexcept {} driver error!'.format(str(e)))
        driver.quit()

    # set the test scope, the full scopes should also contains class, package, module
    scope = request.node
    if type(scope) == pytest.Session:
        for item in scope.items:
            cls = item.getparent(pytest.Class)
            # register driver
            setattr(cls.obj, 'driver', driver)
    elif type(scope) == pytest.Function:
        cls = scope.getparent(pytest.Class)
        setattr(cls.obj, 'driver', driver)

    try:
        log.info('open url: {}'.format(url))
        driver.get(url)
    except Exception as e:
        log.error('unexpected error {}'.format(str(e)))

    log.info('set the implicitly wait to {} seconds'.format(implicitly_wait))
    driver.implicitly_wait(implicitly_wait)

    log.info('start test')
    yield

    log.info('end test')
    driver.quit()
