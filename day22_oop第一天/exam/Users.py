# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/31 07:18
# 文件名称: Users.py

class Users(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password


alex = Users('alex', '123456')
taibai = Users('taibai', '123456')
print(alex.__dict__)
print(taibai.__dict__)
# {'name': 'alex', 'password': '123456'}
# {'name': 'taibai', 'password': '123456'}