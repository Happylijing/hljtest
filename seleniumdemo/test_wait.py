# -*- coding: utf-8 -*-
# @Time:2024/5/31 19:55
# @Author：huanglijing

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://ceshiren.com/")
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="按类别分组的所有话题"]').click()

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        # presence_of_element_located直到元素出现
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()

    def test_baidu(self):
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹学院")

        # presence_of_element_located直到元素出现
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="kw"]')))
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹学院")
        sleep(3)
        self.driver.find_element(By.ID, 'su').click()
