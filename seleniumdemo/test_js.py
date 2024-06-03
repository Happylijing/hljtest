# -*- coding: utf-8 -*-
# @Time:2024/6/3 14:31
# @Author：huanglijing
from seleniumdemo.base import Base
from time import sleep
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 滑动到底部
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()  # 点击【下一页】
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 滑动到底部
        sleep(3)

        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")  # 打开12306网址
        self.driver.execute_script(
            "a=document.getElementById('train_date'); a.removeAttribute('readonly')")  # 定位到出发日期控件,移除readonly属性
        self.driver.execute_script("document.getElementById('train_date').value='2024-06-04'")  # 修改日期为2024-06-04
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))  # 打印修改后的日期
