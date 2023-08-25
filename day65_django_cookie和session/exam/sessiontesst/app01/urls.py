# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/8/25 07:26

from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.App01View.as_view(), name='index'),
    path('home/', views.App01View.as_view(), name='home'),
    path('upload/', views.App01View.as_view(), name='upload'),
    # path('logout/', views.App01View.as_view(), name='logout'),
]