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
import pytest
from utils import path_parser, config_parser


class Runner(object):

    def __init__(self):
        self.pp = path_parser.PathParser()
        self.cp = config_parser.ConfigParser()
        self.tests_dir = self.pp.get_tests_path()
        self.report_dir = self.pp.get_report_path()
        self.html_report_dir = self.pp.get_html_report_path()
        self.screenshots_dir = self.pp.get_screen_shots_path()
        self.rerun_failures = self.cp.get_rerun_failures()
        self.rerun_delay = self.cp.get_rerun_delay()
        self.pp.remove_dirs(self.report_dir, self.screenshots_dir)

    def run_test(self):
        self.generate_results()
        self.generate_html_report()

    def generate_results(self):
        pytest.main([self.tests_dir, '--reruns', self.rerun_failures, '--reruns-delay', self.rerun_delay,
                     '--alluredir={}'.format(self.report_dir)])

    def generate_html_report(self):
        cmd = 'allure generate {} -o {}'.format(self.report_dir, self.html_report_dir)
        print(cmd)
        os.system(cmd)


def runner():
    run = Runner()
    run.run_test()


if __name__ == '__main__':
    runner()
