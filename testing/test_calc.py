# -*- coding: utf-8 -*-
# @Time:2024/5/29 21:42
# @Author：huanglijing
import pytest
import yaml

from pythoncode.calculator import Calculator


def test_a():
    print("test case a")


class TestCalc:
    # 类中调用全部方法前，运行一次
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()  # 实例化被测类,实例变量self.calc

    # 类中调用全部方法后，运行一次
    def teardown_class(self):
        print("计算结束")

    # 类中每次调用方法前，打印计算开始
    def setup(self):
        print("调用方法前，打印计算开始")

    # 类中每次调用方法后，打印计算结束
    def teardown(self):
        print("调用方法后，打印结束结束")

    # 加
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testdata/test_add_data.yaml")),
                             ids=yaml.safe_load(open(
                                 "testdata/test_ids_add_data.yaml")))
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # 减
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testdata/test_sub_data.yaml")),
                             ids=yaml.safe_load(open(
                                 "testdata/test_ids_add_data.yaml")))
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # 乘
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testdata/test_mul_data.yaml")),
                             ids=yaml.safe_load(open(
                                 "testdata/test_ids_add_data.yaml")))
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # 除
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testdata/test_div_data.yaml")),
                             ids=yaml.safe_load(open(
                                 "testdata/test_ids_add_data.yaml")))
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # def test_add1(self):
    #     test_data = [
    #     [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-0.1, -0.1, -0.2], [1, 0, 1]]
    #     for i in range(0, len(test_data)):
    #         # calc = Calculator()  # 实例化被测类
    #         result = self.calc.add(test_data[i][0], test_data[i][1])  # 调用被测类的方法
    #         assert result == test_data[i][2]  # 断言被测方法的结果是否符合预期

    # def test_add2(self):
    #     # calc = Calculator()  # 实例化被测类
    #     result = self.calc.add(0.1, 0.1)  # 调用被测类的方法
    #     assert result == 0.2  # 断言被测方法的结果是否符合预期
