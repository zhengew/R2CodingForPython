# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm综合练习题.py
# @datatime: 2023/7/30 22:53

import os
import django
import pymysql
import pymysql.constants.ER

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models
    from django.db.models import Avg, Max, Min, Sum, Count, F, Q
    from django.db import connection, connections

    # 1 查询每个作者的姓名以及出版的书的最高价格
    # ret = models.Book.objects.values('authors__name').annotate( maxPrice=Max('price'))
    # print(ret) # <QuerySet [{'authors__name': '张爱玲', 'maxPrice': Decimal('140.990000')}, {'authors__name': '金庸', 'maxPrice': Decimal('118.367500')}]>
    #
    # ret = models.Author.objects.values('name').annotate(maxPrice=Max('book__price')).values('name', 'maxPrice').exclude(maxPrice=None)
    # print(ret)
    #
    # ret = models.Author.objects.annotate(maxPrice=Max('book__price')).values('name', 'maxPrice').exclude(maxPrice=None)
    # print(ret)

    '''
    select 
        a.name as authorName, max(b.price) as maxPrice
     from root_book b 
     inner join root_book_authors ba on b.id = ba.book_id
     inner join root_author a on ba.author_id = a.id
     group by a.name
    '''

    # 2 查询作者id大于2作者的姓名以及出版的书的最高价格
    # ret = models.Book.objects.filter(authors__id__gt=2).values('authors__name').annotate(maxPrice=Max('price'))
    # print(ret) # <QuerySet [{'authors__name': '金庸', 'maxPrice': Decimal('130.99')}, {'authors__name': '张爱玲', 'maxPrice': Decimal('140.99')}]>

    # ret = models.Author.objects.filter(id__gt=2).annotate(maxPrice=Max('book__price')).values('name', 'maxPrice')
    # print(ret)

    '''
    select 
        a.name as authrName, max(b.price) as MaxPrice 
     from root_book b 
     inner join root_book_authors ba on b.id = ba.book_id 
     inner join root_author a on ba.author_id = a.id 
     where a.id > 2
     group by a.name  
    '''

    # 3 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格
    # ret = models.Book.objects.values('authors__name').filter(Q(authors__id__gt=2), authors__sex='2').annotate(maxPrice=Max('price'))
    # print(ret) # <QuerySet [{'authors__name': '张爱玲', 'maxPrice': Decimal('140.99')}]>

    # ret = models.Author.objects.filter(Q(id__gt=2), sex=2).annotate(maxPrice=Max('book__price')).values('name', 'maxPrice')
    # print(ret) # <QuerySet [{'name': '张爱玲', 'maxPrice': Decimal('140.99')}]>

    # 4 查询每个作者出版的书的最高价格 的平均值
    # ret = models.Book.objects.annotate(maxPrice=Max('price')).values('maxPrice').aggregate(avgPrice = Avg('maxPrice'))
    # print(ret) # {'avgPrice': Decimal('110.773333')}

    # 5 每个作者出版的所有书的最高价格以及最高价格的那本书的名称（通过orm玩起来就是个死题，需要用原生sql）
    sql = '''
        select t.authorName, b.bname as bookName, t.maxPrice
         from 
             (
                 select a.name as authorName, max(b.price) as maxPrice, ba.author_id as authorId
                 from root_book b 
                 inner join root_book_authors ba on b.id = ba.book_id
                 inner join root_author a on ba.author_id = a.id 
                 group by ba.author_id
             ) as t 
         inner join root_book_authors ba  on t.authorId = ba.author_id 
         inner join root_book b on ba.book_id = b.id
         where b.price = t.maxPrice 
    '''

    cur = connection.cursor()
    cur.execute(sql)
    columns = [col[0] for col in cur.description]
    print(columns)
    ret = [dict(zip(columns, row)) for row in cur.fetchall()]
    print(ret)
