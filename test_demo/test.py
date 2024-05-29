# -*- coding: utf-8 -*-
# print("hello")
# int_a = 1
# str_a = "1234567"
# print(str_a)
# # [start:stop:step] [开始:结束:步长]
# a = str_a[0:3:2]
# print(a)

# list1 = [1,2,3,4,5]
# print(list1[0])
# print(list1[0:5:2])

#
# a = 0
# if a == 0:
#     print("a=0")
# else:
#     print("a != 0")


# result = 0
# for i in range(2,101,2):
#     result = result + i
# print(result)

# a = 1
# while a == 1:a = a + 1
# else:
#     print("a != 1")
#     print(a)


# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)


"""
猜数字游戏
计算出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示：大一点、小一点、猜对了
"""
# import random
# computer_num = random.randint(1, 100)
# while True:
#     input_num = input("请输入一个数字：")
#     person_num = int(input_num)
#     if person_num > computer_num:
#         print("小一点")
#     elif person_num < computer_num:
#         print("大一点")
#     elif person_num == computer_num:
#         print("猜对了")
#         break

# 函数的定义函数func1的作用参数a是用来打印
# 位置参数
# def func1(a,b,c):
#    """
#    :param a:
#    :param b:
#    :param c:
#    :return:
#    """
#    # # 使用tab缩进
#    # print("这是一个函数")
#    # # pycharm快捷键 Ctrl+d
#    # print("这是一个参数a", a)
#    # print("这是一个参数b", b)
#    # print("这是一个参数c", c)
#
#     # 不带表达式的retu或者不写return函数，相当于返回None
#    return
#
#
# # 函数的调用
# a = func1(1, 2, 3)
# print(a)

# """
# 调用函数时，如果没有传递参数，则会使用默认参数
# 如果传递参数，则会使用传递的参数
# """
#
# # 定义函数
# def func2(a, b, c, d):
#     print("参数a的值为：", a)
#     print("参数b的值为：", b)
#     print("参数c的值为：", c)
#     print("参数d的值为：", d)
#
# #在调用函数时，使用k=v的方式传参
# #调用函数
# func2(b=1,c=0,d=-1,a=10)

# func2 = lambda x,y: x+y
# print(func2(3, 2))
#
# def func3(x, y):
#     return x+y
#
# print(func3(3, 2))


#
# list1 = [1, 2, 3]
# # list1.append(0)  #末尾加数据
# # list1.insert(0, 9) #指定位置加数据
# # list1.remove(1) #删除数据
# # list1.pop(0)
# list1.reverse()
# print(list1)


# list_square = []
# for i in range(1, 4):
#     list_square.append(i**2)
# print(list_square)
#
# list_square2 = [i**2 for i in range(1,4)]
# print("list_square2", list_square2)
#
#
# list_square3 = [i**2 for i in range(1,4) if i != 1]
# print(list_square3)

#
# list_square4 = []
# # for i in range(1, 4):
# #     for j in range(1, 4):
# #         list_square4.append(i*j)
#
# list_square4 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_square4)

# 元组的定义
# tuple_1 = (1, 2, 3)
# tuple_2 = 1, 2, 3
#
# print(tuple_1, type(tuple_1))
# print(tuple_2, type(tuple_2))

# 元组的不可变特性
# list_1 = [1, 2, 3]
# list_1[0] = "a"
# print(list_1)
#
# a = [1, 2, 3]
# tuple_1 = (1, 2, 3, a)
# # tuple_1[0] = "a" #元组不可变
# tuple_1[3][0] = "a"  # 元组里面嵌套列表，列表是可变的
# print(tuple_1)

# a = [1, 2, 3, "a", "a"]
# # print(a.count("a"))
# print(a.index("a"))  # 输出列表的索引，有重复的以第一个为准

# 定义集合
# a = {1}
# b = set()
# print(len(b))
# print(type(a))
# print(type(b))


# a = {1, 2, 3}
# b = {1, 4, 5}
# # print(a.union(b))  # 并集
# # print(a.intersection(b))  # 交集
# # print(a.difference(b))  # 差集
# # a.add("a")
# # print(a)
#
# # print({i for i in "aaaaasjahfhrihfiaBCHBC"})
# c = "qjjdsjshjajjnsjdcnskckCJNDSCN"
# print(set(c))


# dict1 = {"a": 1, "b": 2}
# dict2 = dict(a=1, b=2)
# print(dict1, type(dict1))
# print(dict2, type(dict2))
# print(dict1.keys())
# print(dict2.values())
# print(dict1.pop("a")) #删除一个键值对
# print(dict1)
# print(dict1.popitem())  # 被随机删除的键值对
# print(dict1)  # 删除掉被随机删除的键值对后，剩余的键值对
# a = {}
# b = a.fromkeys((1, 2, 3), "a")
# print(b)

# print({i: i * 2 for i in range(1, 3)})
