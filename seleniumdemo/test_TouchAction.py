# -*- coding: utf-8 -*-
# @Time:2024/6/2 15:33
# @Author：huanglijing

from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup_method(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        打开URL : http://www.baidu.com
        向搜索框中输入'selenium测试'
        通过 TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """

        input_ele = self.driver.find_element(By.ID, 'kw')
        search_ele = self.driver.find_element_by_id("su")
        input_ele.send_keys("selenium测试")

        action = TouchActions(self.driver)
        action.tap(search_ele)  # 敲击给定的元素
        action.perform()  # 执行所有存储的操作
        action.scroll_from_element(input_ele, 0, 10000).perform()  # 滑动到最底
        sleep(3)
