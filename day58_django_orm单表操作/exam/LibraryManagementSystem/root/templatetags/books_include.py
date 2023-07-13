# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: books_include.py
# @datatime: 2023/7/11 23:23

from django import template

register = template.Library()

@register.inclusion_tag('include_show_books.html')
def show_books(data):

    return {'data': data}