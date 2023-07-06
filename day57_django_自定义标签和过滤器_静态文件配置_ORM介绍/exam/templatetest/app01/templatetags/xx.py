# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: xx.py
# @datatime: 2023/7/3 21:45

from django import template

register = template.Library() # 注册器 register 固定名字


# 不带参数的过滤器
@register.filter
def oo(v1):
    s = v1 + 'xxoo'
    return s


# 带参数的过滤器
@register.filter
def oo2(v1, v2):
    s = v1 + v2
    return s


# 自定义标签
@register.simple_tag
def mytag(v1, v2, v3):
    s = v1 + '和B哥' + v2 + v3
    return s

# inclusion_tag标签
@register.inclusion_tag('inclusiontag.html')
def func(v1):

    return {'data': v1}