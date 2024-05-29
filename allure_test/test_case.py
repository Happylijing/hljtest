# -*- coding: utf-8 -*-
# @Time:2024/5/29 16:50
# @Author：huanglijing
import allure

TEST_CASE_LINK = 'https://www.baidu.com/'


@allure.testcase(TEST_CASE_LINK, "测试链接")
def test_with_testcase_link():
    pass
