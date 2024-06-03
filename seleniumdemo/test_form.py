# -*- coding: utf-8 -*-
# @Time:2024/6/2 16:26
# @Author：huanglijing

from selenium import webdriver
import pytest
from time import sleep

from selenium.webdriver.common.by import By


class TestForm():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_form(self):
        self.driver.find_element_by_name("user[login]").send_keys("17816875664")
        sleep(2)
        self.driver.find_element(By.NAME, "user[password]").send_keys("123")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.custom-control-label').click()
        sleep(2)
        self.driver.find_element(By.NAME, 'commit').click()
        sleep(3)
