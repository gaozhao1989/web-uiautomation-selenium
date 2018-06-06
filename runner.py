#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: runner
@time: 06/06/2018 5:20 PM
'''

import os

from utils import pathFactory, loggingFactory

log = loggingFactory.Log().getLog('Utils')
tests_path = pathFactory.path_join(pathFactory.get_workspace_root_path(), 'tests')
report_path = pathFactory.path_join(pathFactory.get_workspace_root_path(), 'report')


class Runner(object):
    def __init__(self, *args):
        if args[0] == '' or args[0] == 'tests':
            self.test_scope = 'tests'
        else:
            self.test_scope = args[0]

    def run_test(self):
        self.generate_results()
        self.generate_html_report()

    def generate_results(self, pytest_scope=tests_path, results_dir=report_path):
        import pytest
        pytest.main([pytest_scope, '--alluredir=' + results_dir])

    def generate_html_report(self, results_dir=report_path,
                             html_report_dir=pathFactory.path_join(report_path, 'html')):
        cmd = 'allure generate ' + results_dir + ' -o ' + html_report_dir
        log.debug(cmd)
        os.system(cmd)


def runner():
    run = Runner('tests')
    run.run_test()


if __name__ == '__main__':
    runner()
