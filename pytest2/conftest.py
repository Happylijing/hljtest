# -*- coding: utf-8 -*-
# @Time:2024/5/30 17:35
# @Author：huanglijing

import pytest


@pytest.fixture(scope='session', autouse=True)
def conn_db():
    print("完成数据连接 aaaa")
    yield "database"
    print("关闭数据连接 aaaaa")
