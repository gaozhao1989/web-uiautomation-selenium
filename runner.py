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

from utils import pathparserfactory, loggingfactory, configparserfactory

log = loggingfactory.Log().getlog('Utils')
ppf = pathparserfactory.PathParser()
cpf = configparserfactory.ConfigParser()
tests_path = ppf.path_join(ppf.get_workspace_root_path(), 'tests')
report_path = ppf.path_join(ppf.get_workspace_root_path(), 'report')
screenshot_path = ppf.path_join(ppf.get_workspace_root_path(), 'screenshots')
test_scope = cpf.get_test_scope()


class Runner(object):

    def __init__(self, *args):
        if args[0] == '' or args[0] == test_scope:
            self.test_scope = test_scope
        else:
            self.test_scope = args[0]
        ppf.remove_dirs(report_path, screenshot_path)

    def run_test(self):
        self.generate_results()
        self.generate_html_report()

    def generate_results(self, pytest_scope=tests_path, results_dir=report_path):
        import pytest
        pytest.main([pytest_scope, '--alluredir=' + results_dir])

    def generate_html_report(self, results_dir=report_path,
                             html_report_dir=ppf.path_join(report_path, 'html')):
        cmd = 'allure generate ' + results_dir + ' -o ' + html_report_dir
        log.debug(cmd)
        os.system(cmd)


def runner():
    run = Runner('tests')
    run.run_test()


if __name__ == '__main__':
    runner()
