# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: init.py
# @datatime: 2023/9/7 21:23

import django
import os
import hashlib

def get_md5_pwd(sat, password):
    md5 = hashlib.md5(sat.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'middlewaretest.settings')
    django.setup()

    from appRoot import models

    models.UserInfo.objects.create(**{
        'username': 'zew',
        'password': get_md5_pwd('zew', '123456'),
    })