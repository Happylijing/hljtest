# -*- coding: utf-8 -*-
# @Time:2024/6/3 17:23
# @Author：huanglijing
from seleniumdemo.base import Base
from time import sleep


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://www.baidu.com/")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='form']/span[1]/span[1]").click()
        sleep(6)
        self.driver.find_element_by_xpath("//*[@id='form']/div/div[2]/div[2]/input").send_keys(
            "D:\PycharmProjects\hljtest\seleniumdemo\img\微信图片_20240603173035.png")
        sleep(3)
