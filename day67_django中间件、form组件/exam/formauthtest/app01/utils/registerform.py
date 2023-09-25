# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: loginform.py
# @datatime: 2023/9/26 07:05

from django import forms # form组件
from django.core.validators import RegexValidator # 字段正则校验
from django.core.exceptions import ValidationError # 校验错误

class RegisterForm(forms.Form):

    # 文本框
    username = forms.CharField(
        required=True, # 默认必输，非必输显示的改为False
        min_length=6,
        max_length=16,
        label='用户名',
        initial='test1',
        help_text='用户名限制6～16个字符，不能为空',
        error_messages={
            'required': '用户名不能为空',
            'min_length': '长度不能低于6位',
            'max_length': '长度不能大于16位',
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),

    )
