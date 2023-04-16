# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __gt__比较对象属性的大小.py
# @datatime: 2023/4/16 22:45

"""
目标: 鸭子类型 __gt__
当类中实现了 __gt__方法，再使用 > 比较类的实例对象时，总是调用类中的 __gt__方法
"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        """
        :param other: 实例对象
        :return: 如果self.age > other.age,返回True,否则返回False
        """
        return self.age > other.age

if __name__ == '__main__':
    p1 = Person('alex', 19)
    p2 = Person('wusir', 18)
    print(p1 > p2)  # True

    print(p2 > p1)  # False
