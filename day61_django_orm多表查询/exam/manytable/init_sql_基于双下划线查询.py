# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init_sql_基于双下划线查询.py
# @datatime: 2023/7/25 21:31

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manytable.settings')
    django.setup()

    from app01 import models

    # 多表查询
    # 一对一
        # 1. 查询雪飞电话
        # 方式一 正向查询
    # obj = models.Author.objects.filter(name='崔雪飞').values('authorDetail__telephone')
    # print(obj) # <QuerySet [{'authorDetail__telephone': '13711112222'}]>
        # 方式二 反向查询
    # obj = models.AuthorDetail.objects.filter(author__name='崔雪飞').values('telephone', 'author__age')
    # print(obj) # <QuerySet [{'telephone': '13711112222'}]>

        # 2. 查询 哪个老师的电话是 13711112222
        # 正向
    # obj = models.Author.objects.filter(authorDetail__telephone='13711112222').values('name')
    # print(obj) # <QuerySet [{'name': '崔雪飞'}]>

        # 反向
    # obj = models.AuthorDetail.objects.filter(telephone='13711112222').values('author__name')
    # print(obj)  # <QuerySet [{'author__name': '崔雪飞'}]>

    # 一对多
        # 1.查询 计算机组成原理 这本书的出版社是哪个
        # 正向
    # obj = models.Book.objects.filter(title='计算机组成原理').values('publishs__name')
    # print(obj) # <QuerySet [{'publishs__name': '新华出版社'}]>

        # 反向
    # obj = models.Publish.objects.filter(book__title='计算机组成原理').values('name')
    # print(obj) # <QuerySet [{'name': '新华出版社'}]>

        # 2. 新华出版社 出版了哪些书
        # 正向
    # obj = models.Book.objects.filter(publishs__name='新华出版社').values('title')
    # print(obj) # <QuerySet [{'title': '计算机组成原理'}]>
        # 反向
    # obj = models.Publish.objects.filter(name='新华出版社').values('book__title')
    # print(obj) # <QuerySet [{'book__title': '计算机组成原理'}]>

    '''
        总结:
            1.看过滤条件，就是已知的查询条件
    '''

    # 多对多
    # 1. 计算机组成原理 这本书是谁写的
        # 正向
    # obj = models.Book.objects.filter(title='计算机组成原理').values('authors__name')
    # print(obj) # <QuerySet [{'authors__name': '崔雪飞'}, {'authors__name': '杜甫'}]>
        # 反向
    # obj = models.Author.objects.filter(book__title='计算机组成原理').values('name')
    # print(obj) # <QuerySet [{'name': '崔雪飞'}, {'name': '杜甫'}]>

    # 1. 雪飞写了哪些书
        # 正向
    # obj = models.Book.objects.filter(authors__name='崔雪飞').values('title')
    # print(obj) # <QuerySet [{'title': '计算机组成原理'}]>
        # 方向
    # obj = models.Author.objects.filter(name='崔雪飞').values('book__title')
    # print(obj) # <QuerySet [{'book__title': '计算机组成原理'}]>

    # 进阶
    # 1.新华出版社 出版的书的名称以及作者的名字
        # 正向
    # obj = models.Book.objects.filter(publishs__name='新华出版社').values('title', 'authors__name')
    # print(obj) # <QuerySet [{'title': '计算机组成原理', 'authors__name': '崔雪飞'}, {'title': '计算机组成原理', 'authors__name': '杜甫'}]>
        # 反向
    # obj = models.Publish.objects.filter(name='新华出版社').values('book__title', 'book__authors__name')
    # print(obj) # <QuerySet [{'book__title': '计算机组成原理', 'book__authors__name': '崔雪飞'}, {'book__title': '计算机组成原理', 'book__authors__name': '杜甫'}]>

    # obj = models.Author.objects.filter(book__publishs__name='新华出版社').values('book__title', 'name')
    # print(obj) # <QuerySet [{'book__title': '计算机组成原理', 'name': '崔雪飞'}, {'book__title': '计算机组成原理', 'name': '杜甫'}]>

    # 2. 手机号以 137开头的作者出版的所有书籍名称以及出版社名称
    obj = models.AuthorDetail.objects.filter(telephone__startswith='137').values('author__book__title', 'author__book__publishs__name')
    print(obj) # <QuerySet [{'author__book__title': '计算机组成原理', 'author__book__publishs__name': '新华出版社'}]>