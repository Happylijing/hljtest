# -*- coding: utf-8 -*-
# @Time:2024/5/29 21:42
# @Author：huanglijing
import pytest
import yaml

# 解析测试数据文件
def get_datas(key):
    with open("testdata/calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas[key]['datas']
    add_ids = datas[key]['ids']
    print(add_datas)
    print(add_ids)
    return [add_datas, add_ids]


# 解析测试步骤文件
def steps(steps_file, calc, a, b, expect):
    with open(steps_file) as f:
        steps = yaml.safe_load(f)  # 加载yaml文件的数据

    for step in steps:
        if 'add' == step:
            print("step：add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)
        assert expect == result



class TestCalc:
    # # 类中调用全部方法前，运行一次
    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()  # 实例化被测类, 实例变量self.calc
    #
    # # 类中调用全部方法后，运行一次
    # def teardown_class(self):
    #     print("计算结束")

    # # 类中每次调用方法前，打印计算开始
    # def setup(self):
    #     print("调用方法前，打印计算开始")
    #
    # # 类中每次调用方法后，打印计算结束
    # def teardown(self):
    #     print("调用方法后，打印结束结束")

    # 加
    @pytest.mark.parametrize('a, b, expect', get_datas('add')[0], ids=get_datas('add')[1])
    def test_add(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)  # 调用被测类的方法
        result = get_calc.add(a, b)  # 调用被测类的方法
        assert round(result, 2) == expect  # 断言被测方法的结果是否符合预期

    # 减
    @pytest.mark.parametrize('a, b, expect', get_datas('sub')[0], ids=get_datas('sub')[1])
    def test_sub(self, get_calc, a, b, expect):
        # result = self.calc.sub(a, b)  # 调用被测类的方法
        result = get_calc.sub(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # 乘
    @pytest.mark.parametrize('a, b, expect', get_datas('mul')[0], ids=get_datas('mul')[1])
    def test_mul(self, get_calc, a, b, expect):
        # result = self.calc.mul(a, b)  # 调用被测类的方法
        result = get_calc.mul(a, b)  # 调用被测类的方法
        assert round(result, 2) == expect  # 断言被测方法的结果是否符合预期

    # 除
    @pytest.mark.parametrize('a, b, expect', get_datas('div')[0], ids=get_datas('div')[1])
    def test_div(self, get_calc, a, b, expect):
        # result = self.calc.div(a, b)  # 调用被测类的方法
        result = get_calc.div(a, b)  # 调用被测类的方法
        assert result == expect  # 断言被测方法的结果是否符合预期

    # 除-除数为0，直接捕获异常了，不会有结果
    @pytest.mark.parametrize('a, b', get_datas('zerodiv')[0], ids=get_datas('zerodiv')[1])
    def test_zerodiv(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            # self.calc.div(a, b)  # 调用被测类的方法
            get_calc.div(a, b)  # 调用被测类的方法

    def test_add_steps(self, get_calc):
        a = 1
        b = 1
        expect = 2
        steps_file = "steps/add_steps.yml"
        # steps(steps_file, self.calc, a, b, expect)
        steps(steps_file, get_calc, a, b, expect)
        # assert 2 == self.calc.add(1, 1)
        # assert 0 == self.calc.add(-1, 1)
        # assert 3 == self.calc.add1(1, 2)

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

