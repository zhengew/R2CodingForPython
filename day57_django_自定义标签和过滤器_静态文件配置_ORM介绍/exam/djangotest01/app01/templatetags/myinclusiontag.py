# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: myinclusiontag.py
# @datatime: 2023/7/7 22:24

"""
演示 inclusion_tag标签
"""

from django import template

register = template.Library() # 注册器
@register.inclusion_tag('inclusion_tag.html')  # inclusion_tag标签
def myInclusionTag(args):
    return {'args': args}