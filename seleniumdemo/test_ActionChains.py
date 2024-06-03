# -*- coding: utf-8 -*-
# @Time:2024/6/2 14:36
# @Author：huanglijing

from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip  # 跳过不执行
    # 点击
    def test_case_click(self):
        element_click = self.driver.find_element(By.ID, 'su')
        element_doubleclick = self.driver.find_element(By.XPATH, '//*[@id="su"]')
        element_rightclick = self.driver.find_element(By.CSS_SELECTOR, '#su')

        action = ActionChains(self.driver)
        # action.click(element_click)  # 单击
        # action.double_click(element_doubleclick)  # 双击
        action.context_click(element_rightclick)  # 右键
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip  # 跳过不执行
    # 将光标移动到某个元素上
    def test_movetoelement(self):
        ele = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)  # 将光标移动到某个元素上
        action.perform()
        sleep(3)

    # 拖、拽元素
    @pytest.mark.skip
    def test_dragdrop(self):
        ele_drag = self.driver.find_element()
        ele_drop = self.driver.find_element()

        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag, ele_drop).perform()  # 方法1：拖、拽元素
        # action.click_and_hold(ele_drag).release(ele_drop).perform()  # 方法2：拖、拽元素
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()  # 方法3：拖、拽元素
        sleep(3)

    def test_keys(self):
        ele = self.driver.find_element(By.ID, 'kw')

        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(4)
