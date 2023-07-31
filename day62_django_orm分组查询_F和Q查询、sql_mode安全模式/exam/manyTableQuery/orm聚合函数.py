# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm聚合函数.py
# @datatime: 2023/7/30 17:21

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models
    # 使用聚合函数
    from django.db.models import Max, Min, Avg, Count, Sum

    # 计算所有图书的平均价格
    ret = models.Book.objects.all().aggregate(avgPrice=Avg('price'), maxPrice=Max('price'), minPrice=Min('price'), bookNum=Count(1), sumPrice=Sum('price'))
    print(ret) # {'avgPrice': Decimal('83.490000'), 'maxPrice': Decimal('100.99'), 'minPrice': Decimal('60.99'), 'bookNum': 4, 'sumPrice': Decimal('333.96')}
