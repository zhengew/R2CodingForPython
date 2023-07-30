# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm综合练习题.py
# @datatime: 2023/7/30 22:53

import os
import django
import pymysql

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models
    from django.db.models import Avg, Max, Min, Sum, Count, F, Q

    # 1 查询每个作者的姓名以及出版的书的最高价格

    # 2 查询作者id大于2作者的姓名以及出版的书的最高价格

    # 3 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格

    # 4 查询每个作者出版的书的最高价格 的平均值

    # 5 每个作者出版的所有书的最高价格以及最高价格的那本书的名称（通过orm玩起来就是个死题，需要用原生sql）