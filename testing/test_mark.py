# -*- coding: utf-8 -*-
# @Time:2024/5/30 14:23
# @Author：huanglijing

import pytest


@pytest.mark.login
def test_login1():
    print("登录用例1")


@pytest.mark.login
def test_login2():
    print("登录用例2")


@pytest.mark.search
def test_search1():
    print("搜索用例1")


@pytest.mark.search
def test_search2():
    print("搜索用例2")
