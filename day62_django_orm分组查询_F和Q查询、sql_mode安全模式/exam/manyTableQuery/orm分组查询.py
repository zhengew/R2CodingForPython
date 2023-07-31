# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm分组查询.py
# @datatime: 2023/7/30 20:00

import os
import django
import pymysql

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models
    from django.db.models import Avg, Max, Min, Sum, Count, F, Q

    # 分组查询
    # 统计每个出版社出版的书籍的平均价格
    # annotate 在后
    # ret = models.Book.objects.values('publishs__id').annotate(avgPrice = Avg('price'))
    # print(ret) # <QuerySet [{'publishs__id': 1, 'avgPrice': Decimal('100.990000')}, {'publishs__id': 2, 'avgPrice': Decimal('85.990000')}, {'publishs__id': 3, 'avgPrice': Decimal('70.745000')}]>

    # annotate 在前，默认以当前表的id分组
    # ret = models.Publish.objects.annotate(avgPrice=Avg('book__price')).values('name', 'avgPrice')
    # print(ret) # <QuerySet [{'name': '机械工业出版社', 'avgPrice': Decimal('100.990000')}, {'name': '人民邮电出版社', 'avgPrice': Decimal('85.990000')}, {'name': '新华出版社', 'avgPrice': Decimal('70.745000')}]>

    # having 分组后的过滤
    # ret = models.Publish.objects.annotate(avgPrice=Avg('book__price')).values('name', 'avgPrice').filter(avgPrice__gt=90) # 分组后的过滤 having语句
    # print(ret) # <QuerySet [{'name': '机械工业出版社', 'avgPrice': Decimal('100.990000')}]>


    # F 查询
    # 1. 点赞数大于评论数
    # ret = models.Book.objects.filter(good__gt=F('comment')).values('bname')
    # print(ret) # <QuerySet [<Book: 红楼梦魇>, <Book: 天龙八部>]>
    # 2. 查询点赞数 > 评论数+20的书籍
    # ret = models.Book.objects.filter(good__gt=F('comment') + 20).values('bname')
    # print(ret) # <QuerySet [<Book: 天龙八部>]>

    # 3. 书籍表中所有书籍的价格都加上20
    # ret = models.Book.objects.all().update(price=F('price') + 20)
    # print(ret)

    # 查询评论数大于80和点赞数大于80的
    # ret = models.Book.objects.filter(good__gt=80, comment__gt=80)
    # print(ret)

    # Q 查询
    # 查询评论数大于80或者点赞数大于80的
    # ret = models.Book.objects.filter(Q(good__gt=80)|Q(comment__gt=80))
    # print(ret)

    # Q 查询 与或非  & ｜ ～ , & 优先级高
    # ret = models.Book.objects.filter(~Q(good__gte=80)|Q(comment__gt=100))
    # print(ret)

    # Q 嵌套查询，优先级
    # ret = models.Book.objects.filter(Q(Q(good__gt=80) & Q(comment__gt=80))|Q(price__gt=110))
    # print(ret) # <QuerySet [<Book: 红楼梦魇>, <Book: 射雕英雄传>, <Book: 天龙八部>, <Book: 连城诀>]>

    # filter中普通的,连接的&关系必须写在Q方法后面
    # 评论数>80 且 点赞数>80 且 价格>110
    # ret = models.Book.objects.filter(Q(Q(good__gt=80) & Q(comment__gt=80)), price__gt=110)
    # print(ret) # <QuerySet [<Book: 红楼梦魇>, <Book: 天龙八部>]>

    # django 执行原生sql
    from django.db import connection, connections

    cursor = connection.cursor()
    cursor.execute("select * from root_book where id > %s", (2,))
    ret = cursor.fetchall()
    print(ret)

    # 通过 管道 connection 查看sql执行语句
    print(connection.queries)