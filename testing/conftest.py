# -*- coding: utf-8 -*-
# @Time:2024/5/30 17:21
# @Author：huanglijing
from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope="function", params=['tom', 'jerry'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于return 操作
    yield username
    # teardown 操作
    print("登出操作")


@pytest.fixture(scope='session', autouse=True)
def conn_db():
    print("完成数据连接")
    yield "database"
    print("关闭数据连接")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()  # 实例化被测类
    yield calc  # 返回实例变量calc
    print("计算结束")


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    print(type(items))
    # 调整执行用例顺序，反转
    items.reverse()
    # 编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # 添加标签
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item._nodeid:
            item.add_marker(pytest.mark.div)
