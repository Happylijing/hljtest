# -*- coding: utf-8 -*-
# @Time:2024/5/22 20:47
# @Author：huanglijing

# 创建一个人类
# 通过class 关键字，进行定义了一个类
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问的变量，是实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # def set_param(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age

    # 在方法加装饰器，变成类方法
    @classmethod
    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")

    def jump(self):
        print(f"{self.name} is jumping")


# 类方法和实例方法的区别
# 类方法不能访问实例方法，在类方法加装饰器@classmethod后，类就可以访问实例方法
Person.eat()
# zs = Person('zhangsan', 20, 'male', 130)
# zs.eat()


# 类变量和实例变量的区别
# 类变量是需要类来访问，实例变量需要实例来访问
# print(Person.name)
# Person.name = 'tom'
# print(Person.name)
#
#
# zs = Person('zhangsan', 20, 'male', 130)
# print(zs.name)
# zs.name = "lili"
# print(zs.name)


# 类的实例化，创建了一个实例
# zs = Person('zhangsan', 20, 'male', 130)
# ls = Person('lisi', 30, 'male', 150)
# zs.play()
# ls.play()
# # zs.set_param('zhangsan')
# # zs.set_age(20)
# print(f"张三的姓名是：{zs.name},张三的年龄是：{zs.age},性别是：{zs.gender},体重是：{zs.weight}")
# print(f"lisi的姓名是：{ls.name},lisi的年龄是：{ls.age},性别是：{ls.gender},体重是：{ls.weight}")
