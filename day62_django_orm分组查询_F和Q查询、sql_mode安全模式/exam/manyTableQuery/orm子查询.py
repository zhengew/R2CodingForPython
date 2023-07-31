# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm子查询.py
# @datatime: 2023/7/30 15:21

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models

    # 多表子查询
        # 一对一
    '''
                正向查询: author_obj.authorDetail  对象.关联属性名
        Author --------------------------> AuthorDetail
               <--------------------------
               反向查询： author_detail_obj.author  对象.小写类名
    '''
    # 正向
    # 1. 查询金庸的电话
    # author_obj = models.Author.objects.get(name='金庸')
    # print(author_obj.authorDetail.mobile) # 18712341233

    # 反向
    # 1.查询电话号码是谁的 18712341233
    # author_detail_obj = models.AuthorDetail.objects.get(mobile='18712341233')
    # print(author_detail_obj.author.name) # 金庸

        # 一对多
    '''
            正向查询： book_obj.publishs   对象.关联属性
        Book -----------------------> Publish
            反向查询: publish_obj.book_set.all()  对象.小写类名_set
    '''
    # 正向
    # 1.查询 天龙八部 这本书的出版社是哪个
    # book_obj = models.Book.objects.get(bname='天龙八部')
    # print(book_obj.publishs.name) # 人民邮电出版社

    # 反向
    # 1. 人民邮电出版社 出版了哪些书
    # publish_obj = models.Publish.objects.get(name='人民邮电出版社')
    # print(publish_obj.book_set.values('bname')) # <QuerySet [{'bname': '射雕英雄传'}, {'bname': '天龙八部'}]>

        # 多对多关系
    '''
            正向查询： book_obj.authors.all()   对象.属性
        Book -----------------------> Publish
            反向查询: author_obj.book_set.all()  对象.小写类名_set
    '''
    # 正向
    # 1. 射雕英雄传 这本书是谁写的
    book_obj = models.Book.objects.get(bname='射雕英雄传')
    print(book_obj.authors.all().values('name')) # <QuerySet [{'name': '金庸'}]>

    # 反向
    # 1. 金庸写了哪些书
    author_obj = models.Author.objects.get(name='金庸')
    print([book['bname'] for book in author_obj.book_set.all().values('bname')]) # ['射雕英雄传', '天龙八部', '雪山飞狐']
