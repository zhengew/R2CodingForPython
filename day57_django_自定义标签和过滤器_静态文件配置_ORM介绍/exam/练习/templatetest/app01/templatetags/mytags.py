# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: mytags.py
# @datatime: 2023/7/7 下午1:28

"""
演示自定义标签
"""

from django import template

register = template.Library() # 注册器

@register.simple_tag
def showmytag(*args):
    return [i for i in args]