# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: myfilters.py
# @datatime: 2023/7/7 下午1:08

"""
自定义过滤器
"""
from django import template

register = template.Library() # 注册器对象

@register.filter
def upperCase(words: str):
    """
    自定义过滤器，将参数words转换成大写字母
    :param words:
    :return:
    """
    return words.upper()
