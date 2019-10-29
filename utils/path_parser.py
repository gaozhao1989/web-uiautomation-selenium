#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: path_parser
@time: 06/06/2018 9:54 PM
'''

import os, shutil, platform


class PathParser:

    def __init__(self, workspace_name='web-uiautomation-selenium'):
        self.workspace_name = workspace_name

    @staticmethod
    def current_path():
        return os.getcwd()

    def get_workspace_root_path(self):
        present_work_dir = self.current_path()
        while True:
            if present_work_dir.endswith(self.workspace_name):
                break
            else:
                present_work_dir = os.path.dirname(present_work_dir)
        return present_work_dir

    @staticmethod
    def get_abs_path(path):
        return os.path.abspath(path)

    def get_config_file_path(self):
        return self.get_abs_path(self.path_join(self.get_workspace_root_path(), 'config', 'config.ini'))

    def _get_driver(self):
        sysstr = platform.system()
        os_type = None
        if sysstr == 'Windows':
            os_type = 'win'
        elif sysstr == 'Darwin':
            os_type = 'mac'
        elif sysstr == 'linux':
            os_type = 'linux'
        return self.get_abs_path(self.path_join(self.get_workspace_root_path(), 'drivers', os_type))

    def get_chrome_driver(self):
        return self.get_abs_path(self.path_join(self._get_driver(), 'chromedriver'))

    def get_gecko_driver(self):
        return self.get_abs_path(self.path_join(self._get_driver(), 'geckodriver'))

    def get_opera_driver(self):
        return self.get_abs_path(self.path_join(self._get_driver(), 'operadriver'))

    def get_ms_edge_driver(self):
        return self.get_abs_path(self.path_join(self._get_driver(), 'MicrosoftWebDriver'))

    def get_tests_path(self):
        return self.get_abs_path(self.path_join(self.get_workspace_root_path(), 'tests'))

    def get_report_path(self):
        return self.get_abs_path(self.path_join(self.get_workspace_root_path(), 'report'))

    def get_html_report_path(self):
        return self.get_abs_path(self.path_join(self.get_report_path(), 'html'))

    def get_screen_shots_path(self):
        return self.get_abs_path(self.path_join(self.get_workspace_root_path(), 'screenshots'))

    @staticmethod
    def path_join(path, *paths):
        return os.path.join(path, *paths)

    @staticmethod
    def make_dir(path):
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)

    @staticmethod
    def remove_dirs(*paths):
        for path in paths:
            if os.path.exists(path):
                shutil.rmtree(path)
