# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/8/24 20:54

from django.urls import path
from app01 import views

urlpatterns = [
    # app01根路径
    path('', views.App01View.as_view(), name='index'),
    # 主页
    path('home/', views.App01View.as_view(), name='home'),
    # 文件上传
    path('upload/', views.App01View.as_view(), name='upload'),
    # 退出登录
    path('logout/', views.App01View.as_view(), name='logout'),
]