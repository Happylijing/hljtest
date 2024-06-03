# -*- coding: utf-8 -*-
# @Time:2024/5/31 19:05
# @Author：huanglijing

from selenium import webdriver
from time import sleep


class TestHogwards():
    # 初始化环境
    def setup_method(self):
        self.driver = webdriver.Chrome()  # driver初始化
        self.driver.maximize_window()  # 浏览器窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待，动态的等待5秒，全局变量，简化代码

    # 资源回收
    def teardown_method(self):
        self.driver.quit()  # 关闭浏览器

    # 测试用例
    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")  # 打开网址
        self.driver.find_element_by_link_text("社区").click()  # 点击
        self.driver.find_element_by_css_selector(".topic-39637 .title > a").click()
