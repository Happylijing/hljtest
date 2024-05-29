# -*- coding: utf-8 -*-
# @Time:2024/5/21 20:20
# @Author：huanglijing

name = "lili"
age = 20
list1 = [1, 2, 3]
dict1 = {"name": "tom", "gender": "male"}
# print('my name is {1}, age is {0}, {0}{1}{1}'.format(name, age))
# print("my list is {0}, dict is {1}".format(list1, dict1))

namelsit = ["lili", "tom", "jame"]
# print('we name: {}、{}、and {}'.format(*namelsit))  # 列表解包
# print('we name is {name}, gender is {gender}'.format(**dict1))  # 字典解包

print(f"my name is {name}, age is {age}, my list is {list1[0]}, my dict is {dict1['name']}")

print(f"My name is {name.upper()}")

print(f"result is {(lambda x: x + 1)(2)}")

print(f"my age is {111}")
