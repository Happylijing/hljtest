# -*- coding: utf-8 -*-
# @Time:2024/5/29 21:52
# @Author：huanglijing

# 模块级别
def setup_module():
    print("资源准备： setup module")


def teardown_module():
    print("资源准备：teardown module")


def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo:

    # 类前后分别执行setup_class、teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 类方法前后分别执行setup、teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
