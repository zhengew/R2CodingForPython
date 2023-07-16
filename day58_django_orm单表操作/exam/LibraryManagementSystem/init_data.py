# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init_data.py
# @datatime: 2023/7/15 21:41

# 外部文件使用django的models, 需要配置 django环境

import os

if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryManagementSystem.settings') # manage.py 中的 django 项目环境
    import django
    django.setup()  # 启用 django环境


    from root import models

    obj_list = []

    # for i in range(1, 19):
    #     book_Obj = models.Book(
    #         bname = '降龙十八掌第%s式' %i,
    #         price = 100 + i,
    #         publishDate= '2019-07-%s' %i,
    #         publisher='人民邮电出版社' if i < 5 else '机械工业出版社',
    #     )
    #     obj_list.append(book_Obj)
    #
    # models.Book.objects.bulk_create(obj_list)

    user_list = []
    for i in range(1, 20):
        user_obj = models.UserInfo(
            username='test%s' %i,
            password='123456',
        )
        user_list.append(user_obj)

    models.UserInfo.objects.bulk_create(user_list)