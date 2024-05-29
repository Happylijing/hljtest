# -*- coding: utf-8 -*-
# @Time:2024/5/29 18:09
# @Author：huanglijing

import pytest
from selenium import webdriver
import time
import allure


@allure.testcase("https://github.com/")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome(executable_path="D:\SoftWare\ChromeDriver\chromedriver-win32\chromedriver.exe")
        driver.get("https://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./ziyuan/a.png")
        allure.attach.file("./ziyuan/a.png", name="这是截图", attachment_type=allure.attachment_type.JPG)

    with allure.step("关闭浏览器"):
        driver.quit()
