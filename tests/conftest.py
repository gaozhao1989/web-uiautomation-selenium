#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: 449628536@qq.com
@software: web-uiautomation-selenium
@file: conftest.py.py
@time: 2019/1/6 上午12:24
'''

import pytest, requests, json, re


def get_book_st_second_ver_price():
    params = {
        'method': 'getBookData',
        'asin': 'B00114E7RQ'
    }
    res = requests.get('https://www.amazon.cn/gp/search-inside/service-data', params=params)
    return re.search('\d+.\d+', json.loads(res.content)['buyingPrice']).group()


@pytest.fixture(params=['20.40', get_book_st_second_ver_price()])
def order_price_fixture(request):
    return request.param
