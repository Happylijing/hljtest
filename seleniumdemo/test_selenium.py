# -*- coding: utf-8 -*-
# @Time:2024/5/31 16:30
# @Author：huanglijing

from selenium import webdriver
import time


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.quit()
