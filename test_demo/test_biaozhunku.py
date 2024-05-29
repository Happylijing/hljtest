# -*- coding: utf-8 -*-
# @Time:2024/5/23 20:13
# @Author：huanglijing

import os
import time

# os.mkdir("testdir")
# print(os.listdir("./"))
# os.removedirs("testdir")
# print(os.getcwd())  # 获取当前路径地址

# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt", "w")
#     f.write("hello, os using")
#     f.close()
#

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取2天前的时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))

# import urllib.request
#
# response: object = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(response.read())
# print(response.headers)

import math

print(math.ceil(5.4))
print(math.floor(5.1))
print(math.sqrt(9))
