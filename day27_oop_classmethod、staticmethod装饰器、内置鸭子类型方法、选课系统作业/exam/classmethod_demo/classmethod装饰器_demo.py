# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: classmethod装饰器_demo.py
# @datatime: 2023/4/10 20:10
import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        """
        在类中实例化对象
        :return:
        """
        struct_t = time.localtime()
        date = cls(struct_t.tm_year, struct_t.tm_mon, struct_t.tm_mday) # 实例化Date对象
        return date

if __name__ == '__main__':
    d = Date.today()
    print(d.year, d.month, d.day) # 2023 4 10