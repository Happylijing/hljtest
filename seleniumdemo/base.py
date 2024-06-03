# -*- coding: utf-8 -*-
# @Time:2024/6/2 17:07
# @Author：huanglijing

from selenium import webdriver
import os


class Base():
    def setup_method(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
