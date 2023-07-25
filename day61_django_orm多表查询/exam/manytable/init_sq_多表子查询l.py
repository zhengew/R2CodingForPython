# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init_sql.py
# @datatime: 2023/7/25 20:43

import os
import django

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manytable.settings')
    django.setup()

    from app01 import models

    # 多表查询
    # 一对一
        # 正向查询
        # 1. 查询雪飞电话
    # author_obj = models.Author.objects.filter(name='雪飞').first()
    # print(author_obj.authorDetail) # 北京市海淀区后厂村东路
    # print(author_obj.authorDetail.telephone) # 18711112222

        # 反向查询
        # 1. 查询电话号码是谁的 18711112222
    # author_detail_obj = models.AuthorDetail.objects.get(telephone='18711112222')
    # print(author_detail_obj.author) # 雪飞  __str__ return的 self.name
    # print(author_detail_obj.author.name) # 雪飞

    '''
                正向查询: author_obj.authorDetail  对象.关联属性名
        Author --------------------------> AuthorDetail
               <--------------------------
               反向查询： author_detail_obj.author  对象.小写类名
    '''


    # 一对多
        # 正向查询
        # 1.查询 计算机组成原理 这本书的出版社是哪个
    # book_obj = models.Book.objects.get(title="计算机组成原理")
    # print(book_obj.publishs) # 新华出版社
    # print(book_obj.publishs.name) # 新华出版社\

        # 反向查询
        # 1. 新华出版社 出版了哪些书
    # publish_obj = models.Publish.objects.get(name="新华出版社")
    # print(publish_obj.book_set.all()) # <QuerySet [<Book: 计算机组成原理>]>

    '''
            正向查询： book_obj.publishs   对象.属性
        Book -----------------------> Publish
            反向查询: publish_obj.book_set.all()  对象.小写类名_set
    '''

    # 多对多
        # 正向查询
        # 1. 计算机组成原理 这本书是谁写的
    # book_obj = models.Book.objects.get(title='计算机组成原理')
    # print(book_obj.authors.all()) # <QuerySet [<Author: 崔雪飞>, <Author: 杜甫>]>

        # 反向查询
        # 1. 雪飞写了哪些书
    # author_obj = models.Author.objects.get(name='崔雪飞')
    # print(author_obj.book_set.all()) # <QuerySet [<Book: 计算机组成原理>]>

    '''
                正向查询： book_obj.authors.all()   对象.属性
            Book -----------------------> Publish
                反向查询: author_obj.book_set.all()  对象.小写类名_set
        '''

