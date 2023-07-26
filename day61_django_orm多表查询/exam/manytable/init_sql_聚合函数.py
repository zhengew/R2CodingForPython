# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init_sql_聚合函数.py
# @datatime: 2023/7/26 21:05

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manytable.settings')
    django.setup()

    from app01 import models
    from django.db.models import Avg, Max, Min, Sum, Count

    # 计算所有图书的平均价格
    obj = models.Book.objects.all().aggregate(avgPrice = Avg('price'), maxPrice = Max('price'))
    print(obj) # {'price__avg': Decimal('102.000000')}