# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __eq__比较两个对象是否为相等.py
# @datatime: 2023/4/16 22:35

"""
目标: 鸭子类型 __eq__
当类中实现了 __eq__方法，再使用 == 比较类的实例对象时，总是调用类中的 __eq__方法
"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """
        :param other: 实例对象
        :return: 如果姓名和年龄相等，就返回True,否则返回False
        """
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        """
        :param other: 实例对象
        :return: 如果self.age > other.age,返回True,否则返回False
        """
        return self.age > other.age

    def __lt__(self, other):
        """
        :param other: 实例对象
        :return: 如果self.age < other.age,返回True,否则返回False
        """
        return self.age < other.age


if __name__ == '__main__':
    p1 = Person('alex', 18)
    p2 = Person('alex', 18)
    print(p1 == p2) # True

    p3 = Person('alex', 19)
    print(p1 == p3) # False
