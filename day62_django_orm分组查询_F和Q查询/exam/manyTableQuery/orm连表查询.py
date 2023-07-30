# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm连表查询.py
# @datatime: 2023/7/30 16:05

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    from root import models

    # 基于双下划线方法的连表查询

        # 一对一

    # 1. 查询金庸的电话
    # 正向
    # mobile = models.Author.objects.filter(name='金庸').values('authorDetail__mobile')
    # print(mobile) # <QuerySet [{'authorDetail__mobile': '18712341233'}]>

    # 反向
    # mobile = models.AuthorDetail.objects.filter(author__name='金庸').values('mobile')
    # print(mobile) # <QuerySet [{'mobile': '18712341233'}]>

    # 2. 查询 电话号码 18712341233 是谁的
    # 正向
    # name = models.Author.objects.filter(authorDetail__mobile='18712341233').values('name')
    # print(name) # <QuerySet [{'name': '金庸'}]>

    # 反向
    # name = models.AuthorDetail.objects.filter(mobile='18712341233').values('author__name')
    # print(name) # <QuerySet [{'author__name': '金庸'}]>

        # 一对多
    # 1.查询 天龙八部 这本书的出版社是哪个
    # 正向
    # publish_name = models.Book.objects.filter(bname='天龙八部').values('publishs__name')
    # print(publish_name) # <QuerySet [{'publishs__name': '人民邮电出版社'}]>

    # 反向
    # publish_name = models.Publish.objects.filter(book__bname='天龙八部').values('name')
    # print(publish_name) # <QuerySet [{'name': '人民邮电出版社'}]>

    # 2. 新华出版社 出版了哪些书
    # 正向
    # books = models.Book.objects.filter(publishs__name='新华出版社').values('bname')
    # print(books) # <QuerySet [{'bname': '雪山飞狐'}]>

    # 反向
    # books = models.Publish.objects.filter(name='新华出版社').values('book__bname')
    # print(books) # <QuerySet [{'book__bname': '雪山飞狐'}]>

        # 多对多
    # 1. 雪山飞狐 这本书是谁写的
    # 正向
    # author_name = models.Book.objects.filter(bname='雪山飞狐').values('authors__name')
    # print(author_name) # <QuerySet [{'authors__name': '金庸'}]>

    # 反向
    # author_name = models.Author.objects.filter(book__bname='雪山飞狐').values('name')
    # print(author_name) # <QuerySet [{'name': '金庸'}]>

    # 2. 金庸写了哪些书
    # 正向
    # books = models.Book.objects.filter(authors__name='金庸').values('bname')
    # print(books) # <QuerySet [{'bname': '射雕英雄传'}, {'bname': '天龙八部'}, {'bname': '雪山飞狐'}]>

    # 反向
    # books = models.Author.objects.filter(name='金庸').values('book__bname')
    # print(books) # <QuerySet [{'book__bname': '射雕英雄传'}, {'book__bname': '天龙八部'}, {'book__bname': '雪山飞狐'}]>

    # 进阶
    # 1.新华出版社 出版的书的名称以及作者的名字
    # 正向
    # bookName_authorName = models.Book.objects.filter(publishs__name='新华出版社').values('bname', 'authors__name')
    # print(bookName_authorName) # <QuerySet [{'bname': '雪山飞狐', 'authors__name': '金庸'}]>

    # 反向
    # bookName_authorName = models.Publish.objects.filter(name='新华出版社').values('book__bname', 'book__authors__name')
    # print(bookName_authorName) # <QuerySet [{'book__bname': '雪山飞狐', 'book__authors__name': '金庸'}]>

    # 2. 手机号以 187开头的作者出版的所有书籍名称以及出版社名称
    # 正向
    # bookName_publishName = models.Book.objects.filter(authors__authorDetail__mobile__istartswith='187').values('bname', 'publishs__name').distinct()
    # print(bookName_publishName)
    # 反向
    # bookName_publishName = models.AuthorDetail.objects.filter(mobile__startswith='187').values('author__book__bname', 'author__book__publishs__name').exclude(**{'author__book__bname': None})
    # print(bookName_publishName)

    # related_name 约束属性别名
    # 1.查询 天龙八部是哪个出版社出版的
    # 正向
    publishName = models.Book.objects.filter(bname='天龙八部').values('publishs__name')
    print(publishName) # <QuerySet [{'publishs__name': '人民邮电出版社'}]>
    # 反向
    publishName = models.Publish.objects.filter(Publish__bname='天龙八部').values('name')
    print(publishName) # <QuerySet [{'name': '人民邮电出版社'}]>