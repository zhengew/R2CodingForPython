# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: orm多表插入数据.py
# @datatime: 2023/7/30 09:32

import django
import os

if __name__ == '__main__':

    # django 环境
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manyTableQuery.settings')
    django.setup()

    # orm建表
    from root import models

    # 用户表
    # user_lst = []
    # for i in range(1, 11):
    #     obj = models.UserInfo(**{'username': 'test%s'%i, 'password': '123456'})
    #     user_lst.append(obj)
    #
    # models.UserInfo.objects.bulk_create(user_lst)

    # 作者详细信息表
    # authorDetail_lst = []
    # for i in range(1, 10):
    #     obj = models.AuthorDetail(**{'birthday': '1980-01-%s' %i, 'mobile': '1871234123%s' %i, 'address': '北京市海淀区青龙桥街道' if i < 5 else '北京市朝阳区甘露园'})
    #     authorDetail_lst.append(obj)
    #
    # models.AuthorDetail.objects.bulk_create(authorDetail_lst)

    # 作者表
    # models.Author.objects.update_or_create(
    #     name = '辰东',
    #     defaults = {
    #         'name': '辰东',
    #         'sex': '1',
    #         'authorDetail_id':2,
    #     }
    # )

    # models.Author.objects.create(
    #     name = '张爱玲',
    #     sex = '2',
    #     authorDetail_id = 4,
    # )

    # models.AuthorDetail.objects.filter(id=4).update(
    #     birthday = '1920-09-30',
    #     address = '上海市静安区'
    # )

    # 出版社表
    # models.Publish.objects.create(
    #     name = '新华出版社',
    #     city = '上海',
    #     email = 'xh@126.com',
    # )

    # 书籍表
    # models.Book.objects.create(
    #     bname='雪山飞狐',
    #     price = 60.99,
    #     publishDate='1955-01-01',
    #     publishs_id=3,
    # )

    # models.Book.objects.get(id=5).authors.add('5')
