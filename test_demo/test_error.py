# -*- coding: utf-8 -*-
# @Time:2024/5/22 20:07
# @Author：huanglijing

# num = 1
# if num >= 1:
#     print("num <= 1")
# elif num > 100:
#     print("num < 100")
#

# 相除
# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("分母不能为0")
#         return 0
#
# print(div(1, 0))

# 相除
# def div(a,b):
#     return a/b
#
# f = open("data.txt")
#
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[2])
#
#     f.readlines()
#
# except Exception as e:
#     print(e)
#     print("这里一个异常")
#
# else:
#     print("没有异常时执行")
#
# finally:   # finally 最终都会被执行，无论是否有异常
#     print("finally")
#     f.close()


#
#
# list1 = [1, 2, 3]
# print(list1[1])
#
#
# dict1 = {"name":"tom"}
# print(dict1['name'])

# num = input("请输入一个值：")
# print(int(num))


class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误：{num}")
    else:
        print(f"设置的年龄为：{num}")


set_age(-49)
