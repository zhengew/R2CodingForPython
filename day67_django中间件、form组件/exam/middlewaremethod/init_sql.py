# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init_sql.py
# @datatime: 2023/9/21 18:49

import os

import django



if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'middlewaremethod.settings')
    django.setup()

    from app01 import models
    # models.UserInfo.objects.create(
    #     username='zew',
    #     password='123456',
    # )


    # models.Publish.objects.create(
    #     name='新华出版社',
    #     city='深圳',
    #     email='xh@publisher.com',
    # )

    # authorDetail_obj = models.AuthorDetail.objects.get(address__contains='上海')
    # models.Author.objects.create(
    #     name='张爱玲',
    #     author_detail_id=authorDetail_obj.id,
    # )

    # all_publishs = models.Publish.objects.all().order_by('id')
    # print(all_publishs)
