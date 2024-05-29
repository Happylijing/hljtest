# -*- coding: utf-8 -*-
# @Time:2024/5/21 20:52
# @Author：huanglijing

# f = open('data.txt')
# f.readable()
# print(f.readable())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# f.close()

# with 语句快，可以将文件打开后，操作完毕，自动关闭这个文件
# 图片读取需要使用rb,读取二进制的格式
# 正常的文本，可以使用rt，也就是默认格式
wenjian = "data.txt"
with open(wenjian) as f:
    while True:
        line = f.readline().strip('\n')
        if line:
            print(line)
        else:
            break

# import json
# # json 由字典和列表组成的
# data = {
#     "name": ["jame", "hlj"],
#     "age": 19,
#     "gender": "female"
# }
#
# print(type(data))
# data1 = json.dumps(data)  # 将json转为字符串
# print(data1)
# print(type(data1))
#
# data2 = json.loads(data1)  # 将字符串转为json
# print(type(data2))
