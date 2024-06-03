# -*- coding: utf-8 -*-
# @Time:2024/6/3 18:21
# @Author：huanglijing
from selenium.webdriver import ActionChains
from seleniumdemo.base import Base
from time import sleep


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧页面，将元素1拖搜到元素2
        这时候会有一个alert弹框，点击弹框中的'确定'
        然后再按"点击运行"
        关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag_ele = self.driver.find_element_by_id("draggable")
        drop_ele = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()
        sleep(3)

        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
