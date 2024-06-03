# -*- coding: utf-8 -*-
# @Time:2024/6/2 17:06
# @Author：huanglijing
from selenium.webdriver.common.by import By
from time import sleep
from seleniumdemo.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()  # 点击登录
        # print(self.driver.current_window_handle)  # 打印当前窗口
        # print(self.driver.window_handles)  # 打印所有窗口
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__regLink"]').click()  # 点击立即注册
        # print(self.driver.current_window_handle)   # 打印当前窗口
        # print(self.driver.window_handles)   # 打印所有窗口
        windows = self.driver.window_handles  # 获取所有窗口

        self.driver.switch_to_window(windows[-1])  # 跳到最后一个窗口
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("username")  # 输入用户名
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("124555")  # 输入手机号
        sleep(2)

        self.driver.switch_to_window(windows[0])  # 跳到第一个窗口
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)
