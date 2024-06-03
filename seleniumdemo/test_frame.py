# -*- coding: utf-8 -*-
# @Time:2024/6/2 17:47
# @Author：huanglijing
from seleniumdemo.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")  # 切换到要操作的frame下
        drag_ele = self.driver.find_element_by_id("draggable")  # 操作该frame下的请拖拽我的元素
        print(drag_ele.text)  # 打印请拖拽我元素的文字

        # self.driver.switch_to.parent_frame()  # 切换到父frame节点
        self.driver.switch_to_default_content()  # 切换到默认frame节点
        submit_ele = self.driver.find_element_by_id("submitBTN")  # 操作父frame下的点击运行的元素
        print(submit_ele.text)  # 打印点击运行元素的文字
