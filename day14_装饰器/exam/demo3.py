# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/14 07:59
# 文件名称: demo3.py

# 装饰器的应用：登录认证
# 这周的周末作业：模拟博客园登录的作业。装饰器的认证功能。



def login():
    pass


def register():
    pass


status_dict = {
    'username': None,
    'status': False,
}

def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
    :param f:
    :return:
    '''
    def inner(*args,**kwargs):
        '''访问函数之前的操作，功能'''
        print(111)
        ret = f(*args,**kwargs)
        '''访问函数之后的操作，功能'''
    return inner
@auth  # article = auth(article)
def article():
    print('欢迎访问文章页面')
@auth
def comment():
    print('欢迎访问评论页面')
@auth
def dariy():
    print('欢迎访问日记页面')

article()  # inner()
comment()  #inner()
dariy()